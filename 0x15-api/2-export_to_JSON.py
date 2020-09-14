#!/usr/bin/python3
""" export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """  """

    user_id = argv[1]
    res_user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                            format(user_id))
    res_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id))
    user = res_user.json()
    todo = res_todo.json()

    tasks_list = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = user.get("username")
        tasks_list.append(task_dict)

    dict_to_json = {}
    dict_to_json[user_id] = tasks_list
    with open("{}.json".format(user_id), 'w') as json_file:
        json.dump(dict_to_json, json_file)
