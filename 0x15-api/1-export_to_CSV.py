#!/usr/bin/python3
"""
Fetches data from the internet using a API
"""

import csv
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

    csv_data = []
    employee_name = ''

    for employee in employees:
        if employee['id'] == int(sys.argv[1]):
            employee_name = employee['name']
            break

    if len(employee_name) == 0:
        sys.exit()

    for task in employee_todos:
        if task['userId'] == int(sys.argv[1]):
            csv_data.append([sys.argv[1], employee_name,
                             str(task['completed']),
                             task['title']])

    with open('{}.csv'.format(sys.argv[1]), 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(csv_data)
