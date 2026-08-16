#!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API."""

import json
import sys
from urllib import error, request

API_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(url):
    """Fetch JSON data from the given URL."""
    with request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def get_employee(employee_id):
    """Return the employee data for the given ID."""
    return fetch_json(f"{API_URL}/users/{employee_id}")


def get_todo_list(employee_id):
    """Return the todo list for the given employee ID."""
    return fetch_json(f"{API_URL}/todos?userId={employee_id}")


def main():
    """Display the employee todo completion status."""
    if len(sys.argv) != 2:
        return 1

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        return 1

    try:
        employee = get_employee(employee_id)
        todo_list = get_todo_list(employee_id)
    except error.HTTPError:
        return 1

    total_tasks = len(todo_list)
    done_tasks = sum(1 for task in todo_list if task.get("completed") is True)

    print(f"Employee {employee.get('name')} is done with tasks({done_tasks}/{total_tasks}):")

    for task in todo_list:
        if task.get("completed") is True:
            print(f"\t {task.get('title')}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
