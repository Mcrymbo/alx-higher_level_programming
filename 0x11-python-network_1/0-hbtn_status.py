#!/usr/bin/python3
"""
A script that fetches a url
"""
import urllib.request


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as res:
        html = res.read()
        print('Body response:')
        print('    - type: {}'.format(type(html)))
        print('    - content: {}'.format(html))
        print('    - utf8 content: {}'.format(html.decode('utf-8')))
