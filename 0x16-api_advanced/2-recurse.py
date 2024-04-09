#!/usr/bin/python3
"""Code Task 2."""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Code Task 2."""
    import requests

    the_results = requests.get("https://www.reddit.com/r/{}/hot.json"
                               .format(subreddit),
                               params={"count": count, "after": after},
                               headers={"User-Agent": "My-User-Agent"},
                               allow_redirects=False)
    if the_results.status_code >= 400:
        return None

    temp_r = hot_list + [i.get("data").get("title")
                         for i in the_results.json()
                         .get("data")
                         .get("children")]

    info = the_results.json()
    if not info.get("data").get("after"):
        return temp_r

    return recurse(subreddit, temp_r, info.get("data").get("count"),
                   info.get("data").get("after"))

