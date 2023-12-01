#!/usr/bin/python3
"""
fetching url using request package
"""
import requests


if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    text = r.text
    print('Body response:')
    print('    - type: {}'.format(type(text)))
    print('    - content: {}'.format(text))
