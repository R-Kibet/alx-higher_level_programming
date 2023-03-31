#!/usr/bin/python3
""" post email using requests """

import requests
from sys import argv


if __name__ == '__main__':
    data = {'email': argv[2]}
    x = requests.post(argv[1], data)
    print(x.text)
