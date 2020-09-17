#!/usr/bin/python3
""" Acceding and return informacion using API """
import requests


def number_of_subscribers(subreddit):
    """ """
    if subreddit is None:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "luzperdomo"}
    response = requests.get(url, headers=headers)
    json_request = response.json()

    data_subscribers = json_request.get('data', {}).get('subscribers', 0)
    return (data_subscribers)
