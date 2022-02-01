#!/usr/bin/python3
'''
Consume API with Python to export to csv
'''
import csv
from email.quoprimime import quote
import requests
from sys import argv
if __name__ == "__main__":
    employeeID = argv[1]

    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(employeeID)
    employee = requests.get(url)

    route = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    url = route.format(employeeID)
    todoByEmployee = requests.get(url)

    username = employee.json()['username']
    rows = []
    data = {}

    for i in todoByEmployee.json():
        data = {}
        data['USER_ID'] = employeeID
        data['USERNAME'] = username
        data['TASK_COMPLETED_STATUS'] = i['completed']
        data['TASK_TITLE'] = i['title']
        rows.append(data)

    file = '{}.csv'.format(employeeID)

    with open(file, 'w') as f:
        fieldnames = [
            'USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(
            f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)
