#!/usr/bin/python3
""" Class for implimenting area of a square """


class Square:
    """Class Square determines the square of based on size
    """
    def __init__(self, size=0):
        """ Initialize method to initialize the size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Class Method calculates and return square of the object
        """
        return (self.__size ** 2)
