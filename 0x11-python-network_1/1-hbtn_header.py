#!/usr/bin/python3
"""
sends a request to url and displays the value of the
X-request-id variable
"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.info()
        print(html['X-Request-Id'])
