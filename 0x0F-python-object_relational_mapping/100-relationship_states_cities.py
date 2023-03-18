#!/usr/bin/python3
"""
This script shows relationship
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()


def select():
    """
    add a state with cities
    """

    newS = State(name='California')
    newC = City(name='San Francisco', state=newS)
    session.add(newC)
    session.commit()


select()
