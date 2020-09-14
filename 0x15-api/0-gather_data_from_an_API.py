#!/usr/bin/python3
""" Acceding and return informacion using API """
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

    tasks = []
    for task in todo:
        if task.get("completed") is True:
            tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
          len(tasks), len(todo)))

    for task in tasks:
        print("\t {}".format(task))
