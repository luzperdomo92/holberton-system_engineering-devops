#!/usr/bin/python3
""" Acceding and return informacion using API """
import requests


def top_ten(subreddit):
    """ """
    if subreddit is None:
        return 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "luzperdomo"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)
    json_request = response.json()
    data_top = json_request.get('data', {}).get('children', None)
    if data_top:
        for item in data_top:
            print(item.get('data').get('title'))
    else:
        print(None)
