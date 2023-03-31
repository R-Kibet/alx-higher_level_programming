#!/usr/bin/python3
""" requests: errors """
import requests
from sys import argv


if __name__ == '__main__':
    try:
        x = requests.get(argv[1])
        print(x.text)
    except requests.exceptions.RequestException as e:
        print("Error code:{}".format(e.response.text))
