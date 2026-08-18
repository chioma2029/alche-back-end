#!/usr/bin/python3
"""Export an employee's TODO list progress to JSON."""

import json
import os
import sys
from urllib import request

API_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(url):
    """Fetch and decode JSON data from a URL."""
    with request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Export all tasks owned by the given employee to a JSON file."""
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

    username = employee.get("username")
    filename = "{}.json".format(employee_id)
    data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            for task in todos
        ]
    }

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_paths = [
        os.path.join(script_dir, filename),
        os.path.join(os.getcwd(), filename),
    ]

    for output_path in dict.fromkeys(output_paths):
        with open(output_path, "w", newline="", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile)

    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Export an employee's TODO list progress to JSON."""
