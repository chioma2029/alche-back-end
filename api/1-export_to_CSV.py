#!/usr/bin/python3
"""Export an employee's TODO list progress to CSV."""

import csv
import json
import sys
from urllib import request

API_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(url):
    """Fetch and decode JSON data from a URL."""
    with request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Export all tasks owned by the given employee to a CSV file."""
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
    filename = "{}.csv".format(employee_id)

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE",
        ])

        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title"),
            ])

    return 0


if __name__ == "__main__":
    sys.exit(main())
