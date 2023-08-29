#!/usr/bin/python3
"""coordinates of a square"""


class Square:
    """ Class Square that determines the square of by size
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Init method that initializes square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """class method that returns square of the object
        """
        return (self.i__size ** 2)

    @property
    def size(self):
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

    @property
    def position(self):
        """  method used to retrieve position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Method to set position value of square object"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Method to print square according to value of size
        """
        if not self.__size:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end='')
                for k in range(self.size):
                    print("#", end='')
                print()
