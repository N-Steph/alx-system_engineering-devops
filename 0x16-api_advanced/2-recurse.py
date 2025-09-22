#!/usr/bin/python3
"""Implementation of the recurse function"""

import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list of all hot articles of a subreddit"""
    params = {}
    headers = {
        "User-Agent": "recurse"
    }
    if (len(hot_list) != 0 and hot_list[-1] == ""):
        del hot_list[-1]
        return hot_list
    elif (len(hot_list) != 0 and hot_list[-1] != ""):
        params["after"] = hot_list[-1]
        del hot_list[-1]

    api_endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(api_endpoint,
                            params=params,
                            headers=headers,
                            allow_redirects=False)
    print(response.status_code)
    if (response.status_code == 200):
        for post in response.json()["data"]["children"]:
            hot_list.append(post["data"]["title"])
        hot_list.append(response.json()["data"]["after"])
        return recurse(subreddit, hot_list)
    else:
        if (len(hot_list) != 0):
            return hot_list
        return None
