#!/usr/bin/python3
"""
Module to inherits from class BaseGeometry (7-base_geometry)

"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initializes width and height """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
