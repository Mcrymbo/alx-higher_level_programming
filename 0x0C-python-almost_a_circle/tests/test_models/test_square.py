#!/usr/bin/python3
""" test module for Square class """

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
from unittest import TestCase


class TestSquareMethod(unittest.TestCase):
    """ test suit for Rectangle class """

    def setUp(self):
        """ invoked for each test """
        Base._Base__nb_objects = 0

    def test_Sqaure(self):
        """ testing new recangle """

        rect = Square(4)
        self.assertEqual(rect.size, 4)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 1)

    def test_Square_1(self):
        """ testing new recangle """
        rect1 = Square(2)
        rect2 = Square(2)
        self.assertEqual(False, rect2 is rect1)
        self.assertEqual(False, rect1.id == rect2.id)

    def test_Square_2(self):
        """ test with all arguments """
        rect = Square(2, 4, 7, 5)
        self.assertEqual(rect.size, 2)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 7)
        self.assertEqual(rect.id, 5)

    def test_Square_is_instance(self):
        """test if rectangle is instance of base """
        rect = Square(1)
        self.assertEqual(True, isinstance(rect, Base))

    def test_Square_is_instance_of_Rectangle(self):
        """ test if square is instance of Rectangle """

        square = Square(1)
        self.assertEqual(True, isinstance(square, Rectangle))

    def test_no_argument_passed(self):

        """test if no argument is passed to Rectangle """
        with self.assertRaises(TypeError):
            rect = Square()

    def test_too_many_arguments_passed(self):
        """ more than requirened number of arguments passed """

        with self.assertRaises(TypeError):
            square = Square(1, 1, 1, 1, 1)

    def test_access_width(self):
        square = Square(1)
        with self.assertRaises(AttributeError):
            square.__width

    def test_access_height(self):
        square = Square(1)
        with self.assertRaises(AttributeError):
            square.__height

    def test_access_x(self):
        square = Square(1)
        with self.assertRaises(AttributeError):
            square.__x

    def test_access_y(self):
        square = Square(1)
        with self.assertRaises(AttributeError):
            square.__y

    def test_validate_attr_1(self):
        """ pass width as string """
        with self.assertRaises(TypeError):
            square = Square("1", 1)

    def test_validate_attr_2(self):
        """ pass height as string """
        with self.assertRaises(TypeError):
            square = Square(1, "1")

    def test_validate_attr_3(self):
        """ pass x as string """
        with self.assertRaises(TypeError):
            square = Square(1, 1, "1", 1)

    def test_val_1(self):
        """ pass invalid value for width """
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_value_size(self):
        """ test for negative size """

        with self.assertRaises(ValueError):
            square = Square(-1)

    def test_val_2(self):
        """ pass invalid value for height """
        with self.assertRaises(ValueError):
            square = Square(1, -1)

    def test_val_3(self):
        """ pass invalid x value """
        with self.assertRaises(ValueError):
            square = Square(1, 1, -2)

    def test_area_1(self):
        """ test return value of area method """
        sq = Square(2)
        self.assertEqual(sq.area(), 4)
        sq = Square(6)
        self.assertEqual(sq.area(), 36)
        sq = Square(5)
        self.assertEqual(sq.area(), 25)

    def test_display(self):
        """ test display method withing square """

        square = Square(3)
        result = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            square.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_2(self):
        """test diaplay method """
        square = Square(2)
        result = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            square.display()
            self.assertEqual(str_out.getvalue(), result)

        square.size = 6
        result = "######\n######\n######\n######\n######\n######\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            square.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str(self):
        """ tests return value of __str__ """

        square = Square(4, 6, 3, 2)
        result = "[Square] (2) 6/3 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square)
            self.assertEqual(str_out.getvalue(), result)

        square = Square(5, 4, 6, 1)
        result = "[Square] (1) 4/6 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square)
            self.assertEqual(str_out.getvalue(), result)

        square.id = 2
        square.size = 8
        result = "[Square] (2) 4/6 - 8\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square)
            self.assertEqual(str_out.getvalue(), result)

        square = Square(5)
        result = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square)
            self.assertEqual(str_out.getvalue(), result)

        square = Square(4, 7, 2)
        result = "[Square] (2) 7/2 - 4"
        self.assertEqual(square.__str__(), result)

    def test_to_dictionary(self):
        """ returning dictionary """
        square = Square(2, 3, 4, 5)
        result = "[Square] (5) 3/4 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(square)
            self.assertEqual(str_out.getvalue(), result)

        self.assertEqual(square.size, 2)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.height, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)
        self.assertEqual(square.id, 5)

        result = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(square.to_dictionary()))
            self.assertEqual(str_out.getvalue(), result)

    def test_to_json(self):
        """ test obj to JSON string """

        sq = Square(2)
        dct = sq.to_dictionary()
        json_dictionary = Base.to_json_string([dct])
        result = "[{}]\n".format(dct.__str__())
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), result.replace("'", "\""))

    def test_json_file(self):
        """ tests obj to JSON """

        sq = Square(3)
        dct = sq.to_dictionary()
        json_dictionary = Base.to_json_string([dct])
        result = "[{}]\n".format(dct.__str__())
        result = result.replace("'", "\"")

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), result)

        Square.save_to_file([sq])
        result = "[{}]".format(dct.__str__())
        result.replace("'", "\"")
        with open("Square.json", "r") as f:
            ressult1 = f.read()
        self.assertEqual(result, result)

    def test_update(self):
        """ testing update method """

        sq = Square(4)
        result = "[Square] (1) 0/0 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), result)
        sq.update(5)
        result = "[Square] (5) 0/0 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), result)

    def test_update_1(self):
        """ testing update method """

        sq = Square(1)
        result = "[Square] (1) 0/0 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), result)

        sq.update(3, 4, 5, 6)
        result = "[Square] (3) 5/6 - 4\n"
        with patch("sys.stdout", new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), result)
        sq.update(y=3)
        result = "[Square] (3) 5/3 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), result)
        sq.update(id=1, size=5)
        result = "[Square] (1) 5/3 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), result)

    def test_update_dictionary(self):
        """ test update method with dictionary """

        sq = Square(5)
        result = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), result)

        dct = {'size': 2, 'x': 3}
        sq.update(**dct)
        result = "[Square] (1) 3/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq)
            self.assertEqual(str_out.getvalue(), result)

        dct = {'id': 10, 'x': '3', 'y': 5}
        with self.assertRaises(TypeError):
            sq.update(**dct)

    def test_create(self):
        """ used to test create method """

        dictionary = {'id': 98}
        sq = Square.create(**dictionary)
        self.assertEqual(sq.id, 98)

        dictionary = {'id': 98, 'size': 2}
        sq = Square.create(**dictionary)
        self.assertEqual(sq.id, 98)
        self.assertEqual(sq.size, 2)

        dictionary = {'id': 98, 'size': 2, 'x': 3}
        sq = Square.create(**dictionary)
        self.assertEqual(sq.id, 98)
        self.assertEqual(sq.size, 2)
        self.assertEqual(sq.x, 3)

        dictionary = {'id': 98, 'size': 2, 'x': 3, 'y': 2}
        rect = Square.create(**dictionary)
        self.assertEqual(rect.id, 98)
        self.assertEqual(rect.size, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 2)

    def test_load_from_file_1(self):
        """ test load_from_file method """

        sq = Square(7)
        sq2 = Square(2, 3, 4)

        list_rect = [sq, sq2]
        Square.save_to_file(list_rect)
        list_out = Square.load_from_file()
        for i in range(len(list_rect)):
            self.assertEqual(list_rect[i].__str__(), list_out[i].__str__())
