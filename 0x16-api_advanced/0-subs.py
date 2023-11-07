#!/usr/bin/python3
"""Script to query subscribers on passed Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers

    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit given, function returns 0."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
