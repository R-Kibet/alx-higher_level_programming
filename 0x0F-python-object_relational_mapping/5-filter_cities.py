#!/usr/bin/python3

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
    crs.execute("""SELECT cities.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC""", (argv[4], ))
    r = crs.fetchall()

    idx = 0
    for i in r:
        if idx != 0:
            print(", ", end="")
        print("%s" % i, end="")
        idx += 1
    print("")
