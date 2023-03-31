#!/usr/bin/python3
""" headers in urllib """

import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as res:
        x = res.info()
        print(x.get('X-Request-Id'))
