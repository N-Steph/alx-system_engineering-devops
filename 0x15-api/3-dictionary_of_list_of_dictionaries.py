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

    try:
        employee_todos = requests.get(employee_todos_url).json()
        employees = requests.get(employee_id_url).json()
    except requests.exceptions.RequestException:
        sys.exit()

    dict_data = {}

    for employee in employees:
        task_info = []
        for task in employee_todos:
            if employee['id'] == task['userId']:
                new_dict = {"username": employee['username'],
                            "task": task['title'],
                            "completed": task['completed']}
                task_info.append(new_dict)
        dict_data["{}".format(employee['id'])] = task_info

    json_file = open('todo_all_employees.json', 'w')
    json.dump(dict_data, json_file)
    json_file.close()
