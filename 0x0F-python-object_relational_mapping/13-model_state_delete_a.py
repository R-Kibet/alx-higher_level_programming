#!/usr/bin/python3

import sqlalchemy
import sys
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


def delete():
    """
    contains 'a'
    """

    state = session.query(State).filter(State.name.contains('a'))

    for i in state:
        session.delete(i)
    session.commit()


delete()