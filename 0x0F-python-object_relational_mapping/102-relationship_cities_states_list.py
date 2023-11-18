#!/usr/bin/python3
"""
lists all city object from a database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
