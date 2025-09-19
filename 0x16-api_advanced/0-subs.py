#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
	"""Returns the number of subscribers in a subreddit"""
	response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
	if (response.status_code == 200):
		data = response.json()
		return data["data"]["subscribers"]
	else:
		return 0 

