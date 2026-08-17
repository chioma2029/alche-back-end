#!/usr/bin/python3
"""Gather an employee TODO progress from a REST API."""

import json
import sys
from urllib import request

API_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(url):
    """Fetch and decode JSON data from a URL."""
    with request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Print the TODO completion status for the given employee ID."""
    if len(sys.argv) != 2:
        return 1

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        return 1

    try:
        employee = fetch_json("{}/users/{}".format(API_URL, employee_id))
        todos = fetch_json("{}/todos?userId={}".format(API_URL, employee_id))
    except Exception:
        return 1

    employee_name = employee.get("name")
    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(todos)
    ))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))

    return 0


if __name__ == "__main__":
    sys.exit(main())

