#!/usr/bin/python3
"""Hot posts alert."""


def top_ten(subreddit):
    """Hot posts alert."""
    import requests

    the_results = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                               .format(subreddit),
                               headers={"User-Agent": "Erick_N"},
                               allow_redirects=False)
    if the_results.status_code >= 300:
        print('None')
    else:
        [print(i.get("data").get("title"))
         for i in the_results.json().get("data").get("children")]

