#!/usr/bin/python3
"""
Fetches data from the internet using a API
"""

import requests
import sys

if __name__ == '__main__':
    employee_todos_url = 'https://jsonplaceholder.typicode.com/todos'
    employee_id_url = 'https://jsonplaceholder.typicode.com/users'
    employee_todos = requests.get(employee_todos_url).json()
    employees = requests.get(employee_id_url).json()

    total_number_of_task = 0
    task_completed = []
    employee_name = ''

    for employee in employees:
        if employee['id'] == int(sys.argv[1]):
            employee_name = employee['name']
            break

    for task in employee_todos:
        if task['userId'] == int(sys.argv[1]):
            if task['completed']:
                task_completed.append(task['title'])
            total_number_of_task += 1

    print('Employee {} is done with task({}/{}):'.format(employee_name,
                                                         len(task_completed),
                                                         total_number_of_task))
    for task in task_completed:
        print(' {}'.format(task))
