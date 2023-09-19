#!/usr/bin/python3
"""
base file for all other classes of this project
"""
import json
import os
import csv
import turtle


class Base:
    """ base for other class files"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON representation of the dictionary """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that saves JSON file to a file
        """

        filename = "{}.json".format(cls.__name__)

        list_dict = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())
        lst = cls.to_json_string(list_dict)

        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(lst)

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns json string

        Args:
            json_tring: string representation of list dictioanries

        Return:
            empty list if json_string is None
            list_representation otherwise
        """

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns instances with all attribtes set

        Args:
            dictionary: kwargs of a dictionary with keys and values
        """

        if cls.__name__ == 'Rectangle':
            new_attr = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_attr = cls(1)
        new_attr.update(**dictionary)
        return new_attr

    @classmethod
    def load_from_file(cls):
        """
        class method that returns list of instances
        """

        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, encoding='utf-8') as f:
            json_string = f.read()
        list_attr = cls.from_json_string(json_string)
        list_inst = [cls.create(**items) for items in list_attr]

        return list_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves a CSV file """

        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            dict_val = [0, 0, 0, 0, 0]
            dict_keys = ['id', 'size', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            dict_val = ['0', '0', '0', '0']
            dict_keys = ['id', 'size', 'x', 'y']

        mat = []
        if list_objs is True:
            for obj in list_objs:
                for i in range(len(dict_keys)):
                    dict_val[i] = obj.to_dictionary()[dict_keys[i]]
                mat.append(dict_val[:])

        with open(filename, 'w', encoding='utf=8') as f:
            csv_write = csv.writer(f)
            csv_write.writerows(mat)

    @classmethod
    def load_from_file_csv(cls):
        """ method that loads object from a file"""

        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r', encoding='utf-8') as f:
            list_attr = csv.reader(f)
            list_csv = list(list_attr)

        if cls.__name__ == "Rectangle":
            dict_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            dict_keys = ['id', 'size', 'x', 'y']

        mat = []
        for elem in list_csv:
            dct = {}
            for key in enumerate(elem):
                dct[dict_keys[key[0]]] = int(key[1])
            mat.append(dct)

        instance_list = []
        for i in range(len(mat)):
            instance_list.append(cls.create(**mat[i]))

        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws rectangle and square using turtle package
        """

        dra = turtle.Turtle()
        dra.screen.bgcolor("#b7312")
        dra.pensize(4)
        dra.shape("turtle")

        dra.color("ffffff")
        for rect in list_rectangles:
            dra.showturtle()
            dra.up()
            dra.goto(rect.x, rect.y)
            dra.down()
            for i in range(2):
                dra.forward(rect.width)
                dra.left(90)
                dra.forward(rect.height)
                dra.left(90)
            dra.hideturtle()

        dra.color("ffffff")
        for sq in list_squares:
            dra.showturtle()
            dra.up()
            dra.goto(sq.x, sq.y)
            dra.down()
            for i in range(2):
                dra.forward(sq.width)
                dra.left(90)
                dra.forward(sq.height)
                dra.left(90)
            dra.hideturtle()

        dra.exitonclick()
