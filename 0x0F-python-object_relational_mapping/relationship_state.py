#!/usr/bin/python3
"""
Class model for creating database using mysqlalchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ class for creating state table """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state")
