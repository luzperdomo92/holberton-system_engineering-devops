#!/usr/bin/python3
""" Acceding and return informacion using API """
import requests

def recurse(subreddit, hot_list=[]):

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "luzperdomo"}
    response = requests.get(url, headers=headers)
    json_request = response.json()
    hot_posts = json_request.get('data', {}).get('children', None)

    if response.status_code != 200:
        return None

    if hot_list == []:
        return None
    else:
        searh_data = hot_list[0]
        list_title = hot_list[1:]
        return searh_data + recurse(list_title)
