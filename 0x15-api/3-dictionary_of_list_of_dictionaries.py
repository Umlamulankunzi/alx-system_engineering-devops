#!/usr/bin/python3
"""
Uses a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests
import sys


if __name__ == "__main__":
    BASE_URL = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(BASE_URL)
    employees = response.json()

    emp_dict = {}
    for employee in employees:
        employee_id = employee.get("id")
        username = employee.get("username")

        todo_url = "{url}/{emp_id}/todos/".format(
            url=BASE_URL, emp_id=employee_id)

        response = requests.get(todo_url)
        todos = response.json()

        emp_dict[employee_id] = []
        for todo in todos:
            emp_dict[employee_id].append({
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            })
    with open("todo_all_employees.json", "w") as f:
        json.dump(emp_dict, f)
