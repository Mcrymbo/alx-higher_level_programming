#!/usr/bin/python3
""" class rectangle thad defines rectangle based on width """


class Rectangle:
    """ defines class Rectangle """

    def __init__(self, width=0, height=0):
        """ initializes with and height """

        self.height = height
        self.width = width

    @property
    def width(self):
        """ gets the width rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of width """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
        return self.__width

    @property
    def height(self):
        """ gets height of a triangle """

        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
        return self.__height
