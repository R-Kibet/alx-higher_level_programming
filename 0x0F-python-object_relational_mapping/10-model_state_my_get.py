#!/usr/bin/python3

import sqlalchemy
from sys import argv
from model_state import Base, State
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
    get state user input
    """

    state = session.query(State).filter(
            State.name == argv[4]).first()
    print('Not found' if not state else state.id)


select()