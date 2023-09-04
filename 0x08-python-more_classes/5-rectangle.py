#!/usr/bin/python3
""" class rectangle thad defines rectangle based on width """


class Rectangle:

    def __init__(self, width=0, height=0):
        """ initializes with and height """

        self.height = height
        self.width = width

    def area(self):
        """ calculates area of a rectangle """

        return self.height * self.width

    def perimeter(self):
        """ calculates perimeter of a rectangle """

        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.height + self.width))

    @property
    def width(self):
        """ gets the width rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of width """

        if not isinstance(value, int):
            raise TypeError("width must be and integer\n")
        elif (value < 0):
            raise ValueError("width must be >=0\n")
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
            raise TypeError("height must be an integer\n")
        elif (value < 0):
            raise ValueError("height must be >= 0\n")
        else:
            self.__height = value
        return self.__height

    def __str__(self):
        """ returns rectangle with # """

        rect = ""
        if (self.width == 0 or self.height == 0):
            return rect

        for i in range(self.height):
            rect += ("#" * self.width) + "\n"
        return rect[:-1]

    def __repr__(self):
        """ returns string representation of instance """

        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """ deletes an instance of the class rectangle """

        print("Bye rectangle...")
