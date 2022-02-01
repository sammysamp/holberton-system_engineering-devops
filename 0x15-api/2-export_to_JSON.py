#!/usr/bin/python3
'''
Consume API with Python to export to csv
'''
import json
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
    export = {}

    for i in todoByEmployee.json():
        data = {}
        data['task'] = i['title']
        data['completed'] = i['completed']
        data['username'] = username
        rows.append(data)

    export[employeeID] = rows

    file = '{}.json'.format(employeeID)

    with open(file, 'w') as f:
        json.dump(export, f)
