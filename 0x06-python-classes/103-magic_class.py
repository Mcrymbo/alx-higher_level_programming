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

    """ Method for calculating area """
    def area(self):
        return ((self.__radius ** 2) * math.pi)

    """ calculates circumference of a square """
    def circumference(self):
        return (self.__size * math.pi * 2)
