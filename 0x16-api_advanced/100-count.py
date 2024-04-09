#!/usr/bin/python3
"""Code The task 3"""


def count_words(subreddit, word_list, tally={}, after=None):
    """Code The task 3"""
    import requests

    the_result = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "Erick_N"},
                            allow_redirects=False)
    if the_result.status_code != 200:
        return None

    datar = the_result.json()

    testr = [child.get("data").get("title")
             for child in datar
             .get("data")
             .get("children")]
    if not testr:
        return None

    word_list = list(dict.fromkeys(word_list))

    if tally == {}:
        tally = {i: 0 for i in word_list}

    for j in testr:
        wrd_seprat = j.split(' ')
        for k in word_list:
            for m in wrd_seprat:
                if m.lower() == k.lower():
                    tally[k] += 1

    if not datar.get("data").get("after"):
        temp = sorted(tally.items(), key=lambda kv: kv[0])
        temp = sorted(tally.items(),
                      key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(i, j)) for i, j in temp if j != 0]
    else:
        return count_words(subreddit, word_list, tally,
                           datar.get("data").get("after"))

