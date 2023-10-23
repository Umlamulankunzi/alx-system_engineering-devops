#!/usr/bin/python3
"""
Uses a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    BASE_URL = "https://jsonplaceholder.typicode.com/users"
    url = "{base_url}/{emp_id}".format(base_url=BASE_URL, emp_id=employee_id)

    response = requests.get(url)
    username = response.json().get('username')
    todo_url = "{url}/todos".format(url=url)
    response = requests.get(todo_url)
    todos = response.json()

    with open("{}.csv".format(employee_id), "w") as f:
        for task in todos:
            f.write(
                '"{}","{}","{}","{}"\n'.format(
                    employee_id, username, task.get("completed"),
                    task.get("title")))
