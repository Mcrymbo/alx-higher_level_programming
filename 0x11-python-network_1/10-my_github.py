#!/usr/bin/python3
"""
uses Github credentials and uses github api to display
your id
"""
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get('id'))
