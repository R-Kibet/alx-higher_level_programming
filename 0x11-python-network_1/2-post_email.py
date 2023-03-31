#!/usr/bin/python3
""" post methd withemail"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    d = parse.urlencode(data)
    fd = d.encode('ascii')
    req = request.Request(sys.argv[1], fd)
    with request.urlopen(req) as res:
        x = res.read()
        print(x.decode('utf-8'))
