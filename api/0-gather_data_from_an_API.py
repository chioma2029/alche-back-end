#!/usr/bin/python3
  """Gather data from a REST API for a given employee's TODO list progress."""
  import requests
  import sys


  if __name__ == "__main__":
      employee_id = sys.argv[1]
      base_url = "https://jsonplaceholder.typicode.com/"

      user = requests.get(base_url + "users/{}".format(employee_id)).json()
      todos = requests.get(
                  base_url + "todos", params={"userId": employee_id}).json()

      employee_name = user.get("name")
      done_tasks = [task for task in todos if task.get("completed")]

      print("Employee {} is done with tasks({}/{}):".format(
                  employee_name, len(done_tasks), len(todos)))
      for task in done_tasks:
          print("\t {}".format(task.get("title")))
