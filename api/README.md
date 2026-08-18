# Alche Back End

This project contains a small Python script that fetches an employee's TODO list progress from a REST API and prints the completed tasks in the required format.

## Project structure

- `api/0-gather_data_from_an_API.py` - script that accepts an employee ID and prints the TODO progress

## Usage

```bash
python api/0-gather_data_from_an_API.py 1
```

This prints the employee name, the number of completed tasks out of the total, and the titles of the completed tasks.

## Requirements

- Python 3
- No external dependency required (`urllib` is used)