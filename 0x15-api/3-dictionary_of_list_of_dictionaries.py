#!/usr/bin/python3
''' API usage '''
import json
import requests


if __name__ == '__main__':
    the_link = 'https://jsonplaceholder.typicode.com/'
    info_custom = requests.get(the_link + 'users').json()
    with open('todo_all_employees.json', 'w') as the_file:
        json.dump({
            customm.get('id'): [{
                "task": x.get('title'),
                "completed": x.get('completed'),
                "username": customm.get('username')
            } for x in requests.get(the_link + 'todos',
                                    params={"userId": customm.get('id')})
                                    .json()]
            for customm in info_custom}, the_file)
