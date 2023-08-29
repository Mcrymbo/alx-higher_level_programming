#!/usr/bin/python3
""" Class for implementing Square as object"""


class Square:
    """Class Sqare - defines square object
    It takes ths size of the square.

    We initialize the size using __init__ method

    """

    def __init__(self, size):
        """Initializes size of square
        We use init method to initialize it
        the size fiels is protected
        """
        self.__size = size
