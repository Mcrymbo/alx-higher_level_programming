#!/usr/bin/python3
""" test module for Rectangle class """

import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
from unittest import TestCase


class TestRectangleMethod(unittest.TestCase):
    """ test suit for Rectangle class """

    def setUp(self):
        """ invoked for each test """
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        """ testing new recangle """

        rect = Rectangle(1, 1)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 1)

    def test_rectangle_1(self):
        """ testing new recangle """
        rect1 = Rectangle(1, 1)
        rect2 = Rectangle(1, 1)
        self.assertEqual(False, rect2 is rect1)
        self.assertEqual(False, rect1.id == rect2.id)

    def test_rectangle_2(self):
        """ test with all arguments """
        rect = Rectangle(1, 2, 7, 7, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 7)
        self.assertEqual(rect.id, 5)

    def test_rectangle_is_instance(self):
        """test if rectangle is instance of base """
        rect = Rectangle(1, 1)
        self.assertEqual(True, isinstance(rect, Base))

    def test_1_args_passed(self):
        """ test if only one argument is passed """
        with self.assertRaises(TypeError):
            rect = Rectangle(1)

    def test_no_argument_passed(self):
        """test if no argument is passed to Rectangle """
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_access_width(self):
        rect = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rect.__width

    def test_access_height(self):
        rect = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rect.__height

    def test_access_x(self):
        rect = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rect.__x

    def test_access_y(self):
        rect = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rect.__y

    def test_validate_attr_1(self):
        """ pass width as string """
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 1)

    def test_validate_attr_2(self):
        """ pass height as string """
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "1")

    def test_validate_attr_3(self):
        """ pass x as string """
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 1, "1", 1, 1)

    def test_validate_attr_4(self):
        """ pass y as string """

        with self.assertRaises(TypeError):
            rect = Rectangle(1, 1, 1, "1", 1)

    def test_val_1(self):
        """ pass invalid value for width """
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 1)

    def test_val_2(self):
        """ pass invalid value for height """
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 0)

    def test_val_3(self):
        """ pass invalid x value """
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 1, -2)

    def test_value_4(self):
        """ width passed as negative """
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 3)

    def test_value_5(self):
        """ width passed as negative """
        with self.assertRaises(ValueError):
            rect = Rectangle(1, -2)

    def test_val_3(self):
        """ pass invalid y value """
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 1, 1, -2)

    def test_area_1(self):
        """ test return value of area method """

        rect = Rectangle(2, 5)
        self.assertEqual(rect.area(), 10)
        rect = Rectangle(3, 6)
        self.assertEqual(rect.area(), 18)
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_display(self):
        """ test display method withing rectangle """

        rect = Rectangle(3, 4)
        result = "###\n###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_2(self):
        """test diaplay method """
        rect = Rectangle(2, 2)
        result = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect.display()
            self.assertEqual(str_out.getvalue(), result)

        rect.width = 6
        result = "######\n######\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str(self):
        """ tests return value of __str__ """

        rect = Rectangle(4, 6, 3, 2)
        result = "[Rectangle] (1) 3/2 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect)
            self.assertEqual(str_out.getvalue(), result)

        rect1 = Rectangle(5, 4, 6, 1, 12)
        result = "[Rectangle] (12) 6/1 - 5/4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect1)
            self.assertEqual(str_out.getvalue(), result)

        rect1.id = 2
        rect1.width = 8
        rect1.height = 13
        result = "[Rectangle] (2) 6/1 - 8/13\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect1)
            self.assertEqual(str_out.getvalue(), result)

        rect = Rectangle(5, 8)
        result = "[Rectangle] (2) 0/0 - 5/8\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect)
            self.assertEqual(str_out.getvalue(), result)

        rect = Rectangle(4, 4)
        result = "[Rectangle] (3) 0/0 - 4/4"
        self.assertEqual(rect.__str__(), result)

    def test_to_dictionary(self):
        """ returning dictionary """
        rect = Rectangle(2, 3, 4, 5, 10)
        result = "[Rectangle] (10) 4/5 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect)
            self.assertEqual(str_out.getvalue(), result)

        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)
        self.assertEqual(rect.id, 10)

        result = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(rect.to_dictionary()))
            self.assertEqual(str_out.getvalue(), result)

    def test_create(self):
        """ used to test create method """

        dictionary = {'id': 98}
        rect = Rectangle.create(**dictionary)
        self.assertEqual(rect.id, 98)

        dictionary = {'id': 98, 'width': 2}
        rect = Rectangle.create(**dictionary)
        self.assertEqual(rect.id, 98)
        self.assertEqual(rect.width, 2)

        dictionary = {'id': 98, 'width': 2, 'height': 3}
        rect = Rectangle.create(**dictionary)
        self.assertEqual(rect.id, 98)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)

        dictionary = {'id': 98, 'width': 2, 'height': 3, 'x': 0}
        rect = Rectangle.create(**dictionary)
        self.assertEqual(rect.id, 98)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 0)

        dictionary = {'id': 98, 'width': 2, 'height': 3, 'x': 0, 'y': 2}
        rect = Rectangle.create(**dictionary)
        self.assertEqual(rect.id, 98)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 2)

    def test_load_from_file(self):
        """ testing loading JSON object from file """

        file_m = Rectangle.load_from_file()
        self.assertEqual(file_m, [])

    def test_load_from_file_1(self):
        """ test load_from_file method """

        rect1 = Rectangle(1, 1)
        rect2 = Rectangle(1, 2, 3, 4)

        list_rect = [rect1, rect2]
        Rectangle.save_to_file(list_rect)
        list_out = Rectangle.load_from_file()
        for i in range(len(list_rect)):
            self.assertEqual(list_rect[i].__str__(), list_out[i].__str__())

    def test_load_from_file_2(self):
        """ test load file """
        
        linput = []
        Rectangle.save_to_file(linput)
        list_out = Rectangle.load_from_file()
        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), list_out[i].__str__())
