#!/usr/bin/python3
""" requests:json """
import requests
from sys import argv


if __name__ == '__main__':
    data = {'q': ""}
    try:
        data['q'] = argv[1]
    except Exception:
        pass

    x = requests.post("http://0.0.0.0:5000/search_user", data)

    try:
        j = x.json()
        if not j:
            print('No result')
        else:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
    except Exception:
        print("Not a valid JSON")
