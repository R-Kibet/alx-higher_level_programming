#!/usr/bin/python3
""" authentication using requests with git api """
from requests import auth, get
from sys import argv


if __name__ == '__main__':
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    basic = auth.HTTPBasicAuth(username, password)
    r = get(url, auth=basic)
    x =r.json()
    print(x.get('id'))
