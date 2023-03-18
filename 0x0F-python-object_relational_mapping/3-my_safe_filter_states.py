#!/usr/bin/python3
"""
This script slect using user input
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
    crs.execute('SELECT * from states WHERE name = %s ORDER BY states.id',
                (argv[4], ))
    r = crs.fetchall()

    for i in r:
        print(i)

    crs.close()
    engine.close()
