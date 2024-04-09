#!/usr/bin/python3
"""Reddit Sub Counter."""


def number_of_subscribers(subreddit):
    """Reddit Sub Counter."""
    import requests

    the_results = requests.get("https://www.reddit.com/r/{}/about.json"
                               .format(subreddit),
                               headers={"User-Agent": "Erick_N"},
                               allow_redirects=False)
    if the_results.status_code >= 300:
        return 0

    return the_results.json().get("data").get("subscribers")

