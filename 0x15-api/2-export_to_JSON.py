#!/usr/bin/python3
''' collect API data '''
import json
import requests
from sys import argv


if __name__ == '__main__':
    the_link = 'https://jsonplaceholder.typicode.com/'
    info_custom = requests.get(the_link +
                               'users/{}'.format(argv[1])).json()
    dutis_custom = requests.get(the_link + 'todos',
                                params={'userId': argv[1]}).json()
    with open('{}.json'.format(argv[1]), 'w') as the_file:
        json.dump({argv[1]: [{
            "task": x.get('title'),
            "completed": x.get('completed'),
            "username": info_custom.get('username')
        } for x in dutis_custom]}, the_file)
