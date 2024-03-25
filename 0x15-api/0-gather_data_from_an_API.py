#!/usr/bin/python3
''' collect data from API '''
import requests
from sys import argv


if __name__ == '__main__':
    the_link = 'https://jsonplaceholder.typicode.com/'
    info_custom = requests.get(the_link + 'users/{}'.format(argv[1])).json()
    duties_custom = requests.get(the_link + 'todos',
                                 params={'userId': argv[1]}).json()
    finished_dut = [task.get('title')
                    for task in duties_custom if task.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'
          .format(info_custom.get('name'),
                  len(finished_dut), len(duties_custom)))
    [print('\t {}'.format(title)) for title in finished_dut]
