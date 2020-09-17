#!/usr/bin/python3
""" Acceding and return informacion using API """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ """
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    headers = {"User-Agent": "luzperdomo"}
    response = requests.get(url, headers=headers)

    if response:
        data = response.json().get('data')
        children = data.get('children')
        after = data.get('after')
        for item in children:
            hot_list.append(item.get('data').get('title'))

        if after is not None and children:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
