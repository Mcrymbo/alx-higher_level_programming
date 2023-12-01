#!/usr/bin/python3
"""
evaluating candidates applying for backend
"""
import requests
import sys


if __name__ == '__main__':
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repository)
    r = requests.get(url)
    json_o = r.json()
    for i in range(10):
        print("{}: {}".format(json_o[i].get('sha'),
                              json_o[i].get('commit').get('author').get('name')))
