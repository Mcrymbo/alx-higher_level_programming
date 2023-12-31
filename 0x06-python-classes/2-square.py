#!/usr/bin/python3
""" Class with size validation """


class Square:
    """ Squre class that defines a square by its size
    """

    def __init__(self, size=0):
        """ Init Method initializes square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
