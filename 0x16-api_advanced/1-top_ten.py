#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Queries Reddit API and prints the titles of the first 10 hot posts

    listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(
        url, headers=headers, params={"limit": 10}, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    for obj in results.get("children"):
        print(obj.get("data").get("title"))
