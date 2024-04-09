#!/usr/bin/python3
"""Reddit sub counter."""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Reddit sub counter."""
    redditor = {'User-Agent': 'Mozilla/5.0'}
    the_link = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit), headers=redditor).json()
    try:
        return the_link.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])

