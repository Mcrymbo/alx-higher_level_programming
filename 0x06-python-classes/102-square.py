#!/usr/bin/python3
""" Class for implimenting square object"""


class Square:
    """ Class Square that determines the square of by size"""

    def __eq__(self, other):
        """ equal to """
        return self.__size == other.__size

    def __ne__(self, other):
        """ not equal to """

        return self.__size != other.__size

    def __gt__(self, other):
        """ greater than """

        return self.__size > other.__size

    def __ge__(self, other):
        """ greater than or equal to """

        return self.__size >= other.__size

    def __lt__(self, other):
        """ less than """

        return self.__size < other.__size

    def __le__(self, other):
        """ less than or equal to """

        return self.__size <= other.__size

    def __init__(self, size=0):
        """ Init method that initializes square object
        """
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """class method that returns square of the object"""
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method that returns the size of value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Method for setting the size of square object"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
