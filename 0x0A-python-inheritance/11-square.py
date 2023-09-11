#!/usr/bin/python3
"""
Module to inherits from class BaseGeometry (7-base_geometry)

"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from Rectangle """

    def __init__(self, size):
        """ Initializes size """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Calculates the area of size """

        return super().area()

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
