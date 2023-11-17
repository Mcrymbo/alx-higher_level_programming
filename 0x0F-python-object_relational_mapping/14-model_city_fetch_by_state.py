#!/usr/bin/python3
"""
prints all city objects from hbtn_0e_State
"""
import sys
from sqlalchemy import create_engine
from model_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()

    cities = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
