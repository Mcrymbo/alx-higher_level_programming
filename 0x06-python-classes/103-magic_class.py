#!/usr/bin/python3
import math
""" Class for margic class """


class MagicClass:
    """ class fo margic class """

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ method for calculating area """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """ calculates circumference of a square """
        return (self.__size * math.pi * 2)
