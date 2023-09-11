#!/usr/bin/python3
"""
Module to implement empty class BaseGeometry

"""


class BaseGeometry:
    """ implements nothing """

    def area(self):
        """ empty area """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the value """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
