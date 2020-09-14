#!/usr/bin/python3
""" export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """  """

    res_user = requests.get("https://jsonplaceholder.typicode.com/users/")
    res_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    user = res_user.json()
    todo = res_todo.json()

    user_dict = {}
    user_name_dict = {}

    for users in user:
        user_id = users.get("id")
        user_dict[user_id] = []
        user_name_dict[user_id] = users.get("username")
           
    for task in todo:
        task_dict = {}
        user_id = task.get("userId")
        task_dict["username"] = user_name_dict.get(user_id)

        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get('completed')
        user_dict.get(user_id).append(task_dict)

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(user_dict, json_file)
