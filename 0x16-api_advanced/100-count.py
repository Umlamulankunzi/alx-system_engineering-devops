#!/usr/bin/python3
"""
API requests with REDDIT
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(
        base_url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return
    data = response.json()

    for post in data["data"]["children"]:
        title = post["data"]["title"].lower()
        for word in word_list:
            if (word.lower() in title and not
                    any(c.isalpha() for c in title.split(word.lower())[0][-1:]
                    + title.split(word.lower())[1][:1])):
                counts[word.lower()] = counts.get(
                    word.lower(), 0) + title.count(word.lower())

    if data["data"]["after"] is not None:
        count_words(subreddit, word_list, data["data"]["after"], counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
