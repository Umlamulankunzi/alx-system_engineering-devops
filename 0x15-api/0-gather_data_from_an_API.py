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
    emp_name = response.json().get("name")

    todo_url = "{url}/todos".format(url=url)
    response = requests.get(todo_url)
    todos = response.json()
    complete = 0
    complete_todos = []

    for todo in todos:
        if todo.get('completed'):
            complete_todos.append(todo)
            complete += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, complete, len(todos)))

    for task in complete_todos:
        print("\t {}".format(task.get('title')))
