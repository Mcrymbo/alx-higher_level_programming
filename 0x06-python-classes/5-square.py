#!/usr/bin/python3
"""Class for implementing square object"""


class Square:
    """ Class Square that determines the square of by size
    """
    def __init__(self, size=0):
        """ Init method that initializes square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """class method that returns square of the object
        """
        return (self.__size ** 2)

    @property
    def size(self, value):
        """ Method that returns the size of value
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Method for setting the size of square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Method to print square according to value of size
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
