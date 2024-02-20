#!/usr/bin/python3
"""
Fetches data from the internet using a API
"""
import json
import requests
import sys

if __name__ == '__main__':
    employee_todos_url = 'https://jsonplaceholder.typicode.com/todos'
    employee_id_url = 'https://jsonplaceholder.typicode.com/users'

    if len(sys.argv) < 2:
        sys.exit()

    try:
        int(sys.argv[1])
    except ValueError:
        sys.exit()

    try:
        employee_todos = requests.get(employee_todos_url).json()
        employees = requests.get(employee_id_url).json()
    except requests.exceptions.RequestException:
        sys.exit()

    employee_name = ''

    for employee in employees:
        if employee['id'] == int(sys.argv[1]):
            employee_name = employee['username']
            break

    if len(employee_name) == 0:
        sys.exit()

    temp = []
    for task in employee_todos:
        if task['userId'] == int(sys.argv[1]):
            new_dict = {"task": task['title'],
                        "completed": task['completed'],
                        "username": employee_name}
            temp.append(new_dict)
    json_file = open("{}.json".format(sys.argv[1]), 'w')
    json.dump({sys.argv[1]: temp}, json_file)
    json_file.close()
