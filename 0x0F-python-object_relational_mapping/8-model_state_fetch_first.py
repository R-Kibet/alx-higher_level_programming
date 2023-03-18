#!/usr/bin/python3
"""
This script list first state
"""

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

    state = session.query(State).where(State.id == 1).order_by(State.id)
    if state is None:
        print("Nothing")
    for i in state:
        print('{}: {}'.format(i.id, i.name))
