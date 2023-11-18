#!/usr/bin/python3
"""
contains class defination of cities
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    class that defines the city object
    """

    __tablename__ = 'cities'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
