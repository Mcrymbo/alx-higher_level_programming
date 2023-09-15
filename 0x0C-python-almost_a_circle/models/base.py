#!/usr/bin/python3
"""
base file for all other classes of this project
"""


class Base:
    """ base for other class files"""

    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
