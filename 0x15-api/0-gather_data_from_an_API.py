#!/usr/bin/python3
"""
Fetches data from the internet using a API
"""

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

    total_number_of_task = 0
    task_completed = []
    employee_name = ''

    for employee in employees:
        if employee['id'] == int(sys.argv[1]):
            employee_name = employee['name']
            break

    if len(employee_name) == 0:
        sys.exit()

    for task in employee_todos:
        if task['userId'] == int(sys.argv[1]):
            if task['completed'] and task['title'] != '':
                task_completed.append(task['title'])
            if task['title'] != '':
                total_number_of_task += 1

    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                         len(task_completed),
                                                         total_number_of_task))
    for task in task_completed:
        print('\t {}'.format(task))
