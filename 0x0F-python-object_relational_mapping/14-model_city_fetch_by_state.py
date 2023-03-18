#!/usr/bin/python3

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

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
    print city
    """

    state = session.query(State, City).join(City).order_by(City.id).all()
    for s, c in state:
        print('{}: ({}) {}'.format(s.name, c.id, c.name))


select()
