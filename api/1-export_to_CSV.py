#!/usr/bin/python3
"""Export employee TODO list progress to CSV format."""
import csv
import requests
import sys


def export_to_csv():
    """Fetch user tasks from API and write to USER_ID.csv."""
    if len(sys.argv) < 2:
        return

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_res = requests.get(f"{url}/users/{user_id}")
    if user_res.status_code != 200:
        return
    user_data = user_res.json()
    username = user_data.get("username")

    # Fetch todos data
    todos_res = requests.get(f"{url}/todos", params={"userId": user_id})
    if todos_res.status_code != 200:
        return
    todos_data = todos_res.json()

    filename = f"{user_id}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                str(user_id),
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    export_to_csv()
