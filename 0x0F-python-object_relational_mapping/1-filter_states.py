#!/usr/bin/python3
"""
This script ouputs data with specific
character
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    connection to database use argv to hide crucial data
    """

    engine = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )

    crs = engine.cursor()
    q = "SELECT * FROM states WHERE name LIKE 'N%'"
    crs.execute(q)
    r = crs.fetchall()

    for i in r:
        print(i)
