#!/usr/bin/python3
''' makes a get request to a REST API '''
import requests
from sys import argv


if __name__ == '__main__':
    the_link = 'https://jsonplaceholder.typicode.com/'
    info_custom = requests.get(the_link +
                               'users/{}'.format(argv[1])).json()
    dutis_custom = requests.get(the_link + 'todos',
                                params={'userId': argv[1]}).json()
    with open('{}.csv'.format(argv[1]), 'w') as the_file:
        for x in dutis_custom:
            sentes = '"{}","{}","{}","{}"\n'.format(
                x.get('userId'),
                info_custom.get('username'),
                x.get('completed'),
                x.get('title'))
            the_file.write(sentes)
