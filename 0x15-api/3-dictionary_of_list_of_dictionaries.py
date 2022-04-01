#!/usr/bin/python3
'''
Consume API with Python to export to csv
'''
import json
import requests
if __name__ == "__main__":
    export = {}
    url = 'https://jsonplaceholder.typicode.com/users/'
    employees = requests.get(url)
    for i in employees.json():
        employeeID = i['id']
        route = 'https://jsonplaceholder.typicode.com/users/{}/todos'
        url = route.format(employeeID)
        todoByEmployee = requests.get(url)

        username = i['username']
        rows = []
        data = {}

        for j in todoByEmployee.json():
            data = {}
            data['task'] = j['title']
            data['completed'] = j['completed']
            data['username'] = username
            rows.append(data)

        export[employeeID] = rows
    file = '{}.json'.format('todo_all_employees')

    with open(file, 'w') as f:
        json.dump(export, f)
