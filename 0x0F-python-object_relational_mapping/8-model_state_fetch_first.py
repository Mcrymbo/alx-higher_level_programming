#!/usr/bin/python3
"""
Prints the first state object from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()

    state = session.query(State).order_by(State.id).first()

    if (state):
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
