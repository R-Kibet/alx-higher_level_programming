#!/usr/bin/python3
""" repo and owner """

from requests import auth, get
from sys import argv


if __name__ == '__main__':
    try:
        repo = argv[1]
        owner = argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        r = get(url)
        json_o = r.json()
        for i in range(0, 10):
            print("{}: {}".format(json_o[i].get('sha'), json_o[i].get('commit')
                                  .get('author').get('name')))
    except Exception:
        pass
