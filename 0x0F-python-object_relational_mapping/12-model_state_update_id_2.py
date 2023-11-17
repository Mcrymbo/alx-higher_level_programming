#!/usr/bin/python3
"""
add State object to the database
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()

    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = 'New Mexico'
        session.commit()
