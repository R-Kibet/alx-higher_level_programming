#!/usr/bin/python3
""" geting headder info """
from sys import argv
import requests


if __name__ == '__main__':
    x = requests.get(argv[1])
    r = x.headers['X-Request-Id']
    print(r)
