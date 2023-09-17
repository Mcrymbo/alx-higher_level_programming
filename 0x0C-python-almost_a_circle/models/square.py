#!/usr/bin/python3
"""
Class that inherits from class Retangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class that inherits from class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".\
                format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """ gets the size """

        return self.width

    @size.setter
    def size(self, value):
        """ sets the value of size """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates the attributes """

        if args is not None and len(args) != 0:
            list_attr = ['id', 'size', 'x', 'y']

            for i in range(len(args)):
                if list_attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                if (key == "size"):
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ dict representation of square attributes """

        list_attr = ['id', 'size', 'x', 'y']
        dict_attr = {}

        for key in list_attr:
            if key == 'size':
                dict_attr[key] = getattr(self, 'width')
            else:
                dict_attr[key] = getattr(self, key)
        return dict_attr
