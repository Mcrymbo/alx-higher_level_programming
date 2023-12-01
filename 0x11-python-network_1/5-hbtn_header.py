#!/usr/bin/python3
"""
sends request and displays the value of X-Request-id
in the response header
"""
import sys
import requests


if __name__ == '__main__':
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except Exception:
        pass
