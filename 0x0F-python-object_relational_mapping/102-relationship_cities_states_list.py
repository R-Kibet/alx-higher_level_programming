#!/usr/bin/python3
"""
This script lists relationship
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

    city = session.query(State, City).join(State).order_by(City.id).all()

    for s, t in city:
        print("{}: {} -> {}".format(t.id, t.name, s.name))
