#!/usr/bin/python3
""" error handling """

from urllib import request, error
import sys


if __name__ == '__main__':
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as res:
            x = res.read().decode('utf-8')
            print(x)
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
