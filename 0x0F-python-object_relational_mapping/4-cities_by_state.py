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
    query = """SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id;"""
    crs.execute(query)
    r = crs.fetchall()

    for i in r:
        print(i)
