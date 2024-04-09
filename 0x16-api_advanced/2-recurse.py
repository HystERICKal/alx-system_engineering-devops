#!/usr/bin/python3
"""Recursive version."""
import requests


def recurse(subreddit, hot_list=[], testr="", tally=0):
    """Recursive version."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    the_agent = {
        "User-Agent": "Erick_N"
    }
    contens = {
        "after": testr,
        "count": tally,
        "limit": 100
    }
    response = requests.get(url, headers=the_agent, params=contens,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    output = response.json().get("data")
    testr = output.get("after")
    tally = tally + output.get("dist")
    for i in output.get("children"):
        hot_list.append(i.get("data").get("title"))

    if testr is not None:
        return recurse(subreddit, hot_list, testr, tally)
    return hot_list

