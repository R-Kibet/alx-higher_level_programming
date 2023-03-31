#!/usr/bin/python3
""" urllib request """
from urllib import request


if __name__ == '__main__':
    with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        x = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(x)))
        print('\t- contnet: {}'.format(x))
        print('\t- utf8 content: {}'.format(x.decode('utf-8')))
