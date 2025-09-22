#!/usr/bin/python3
"""Implementation of the count_word function"""

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
    if (response.status_code == 200):
        for post in response.json()["data"]["children"]:
            hot_list.append(post["data"]["title"])
        hot_list.append(response.json()["data"]["after"])
        return recurse(subreddit, hot_list)
    else:
        if (len(hot_list) != 0):
            return hot_list
        return None


def count_words(subreddit, word_list):
    """
    Prints the number of times each word in word_list
    appears for all hot posts in subreddit
    """
    hot_list = recurse(subreddit, hot_list=[])
    if hot_list is None:
        return
    words = {}
    number_of_times = 0
    for word in word_list:
        for title in hot_list:
            # count number of times word appears
            words_in_title = title.split()
            for wordt in words_in_title:
                if wordt.lower() == word.lower():
                    number_of_times += 1
        # check if key is not already present in words
        # append number_of_times to the dictionary word
        if word.lower() not in words:
            words[word.lower()] = number_of_times
        else:
            words[word.lower()] += number_of_times
        number_of_times = 0
    sorted_words = sorted(words.items(),
                          key=lambda item: item[1],
                          reverse=True)
    for key, value in sorted_words:
        print(f"{key}: {value}")
