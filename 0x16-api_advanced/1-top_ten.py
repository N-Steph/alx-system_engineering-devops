#!/usr/bin/python3
"""Implementation of top_ten function"""

import requests


def top_ten(subreddit):
    """Prints the title of the first 10 hot posts of the subreddit"""
    api_endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {
        'limit': 10
    }
    response = requests.get(api_endpoint, params=params, allow_redirects=False)
    if (response.status_code == 200):
        hot_posts = response.json()["data"]["children"]
        for post in hot_posts:
            print(post["data"]["title"])
    else:
        print("None")
