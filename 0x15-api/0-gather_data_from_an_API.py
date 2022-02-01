#!/usr/bin/python3
'''
Consume API with Python
'''
import requests
from sys import argv
if __name__ == "__main__":
    employeeID = argv[1]

    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(employeeID)
    employee = requests.get(url)

    route = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    url = route.format(employeeID)
    todoByEmployee = requests.get(url)

    name = employee.json()['name']
    completed = 0
    tasks = 0

    for i in todoByEmployee.json():
        tasks += 1
        if i['completed']:
            completed += 1
    text = 'Employee {} is done with tasks({:d}/{:d}):'
    print(text.format(name, completed, tasks))
    for i in todoByEmployee.json():
        if i['completed']:
            print('\t {}'.format(i['title']))
