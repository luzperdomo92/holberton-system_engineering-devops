#!/usr/bin/python3
""" export data in the CSV format. """
import csv
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

    with open("{}.csv".format(user_id), mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([user_id, user.get('username'),
                            task.get('completed'), task.get('title')])
