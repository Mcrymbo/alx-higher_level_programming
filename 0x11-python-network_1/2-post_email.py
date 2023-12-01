#!/usr/bin/python3
"""
sends post request to the passed url with email as
parameter
"""
from urllib import request, parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
