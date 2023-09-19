#!/usr/bin/python3
"""
implements class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ calculates area of the rectangle """

        return self.height * self.width

    def display(self):
        """ prints character # """

        res = self.y * "\n"
        for i in range(self.height):
            res += (" " * self.x)
            res += ('#' * self.__width) + "\n"
        print(res, end="")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".\
                format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns argument to each attribute """
        if args is not None and len(args) != 0:
            list_attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns dictionary representation of a rectangle """

        list_attr = ['id', 'width', 'height', 'x', 'y']
        dict_attr = {}
        for key in list_attr:
            dict_attr[key] = getattr(self, key)

        return dict_attr
