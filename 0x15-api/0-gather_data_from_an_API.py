#!/usr/bin/python3
""" Acceding and return informacion using API """
import requests
import sys


if __name__ == "__main__":
    """  """

id = int(sys.argv[1])
res_user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
res_todo = requests.get("https://jsonplaceholder.typicode.com/todos?usersId={}"
                        .format(id))
users = res_user.json()
todos = res_todo.json()

tasks = []
for task in todos:
    if task["completed"] is True:
        tasks.append(task["title"])
print("Employee {} is done with tasks {}/{}:".format(users["name"], 
      len(tasks), len(todos)))

for task in tasks:
    print("\t {}".format(task))
