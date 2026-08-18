#!/usr/bin/python3
"""Export all employee TODO lists to a single JSON file."""

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
    """Export all tasks for all employees to a JSON file."""
    if len(sys.argv) != 1:
        return 1

    try:
        users = fetch_json("{}/users".format(API_URL))
        todos = fetch_json("{}/todos".format(API_URL))
    except Exception:
        return 1

    user_map = {str(user.get("id")): user.get("username") for user in users}
    data = {}

    for task in todos:
        user_id = str(task.get("userId"))
        if user_id not in data:
            data[user_id] = []

        data[user_id].append({
            "username": user_map.get(user_id),
            "task": task.get("title"),
            "completed": task.get("completed"),
        })

    filename = "todo_all_employees.json"
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
