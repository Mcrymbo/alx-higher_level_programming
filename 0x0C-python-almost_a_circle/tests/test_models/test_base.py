#!/usr/bin/python3
""" test module for Base class """
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestMaseMethods(unittest.TestCase):
    """ test suit for Base class """

    def setUp(self):
        """ method being invoked for each test """

        Base._Base__nb_objects = 0

    def test_default_id(self):
        """ testing default id """

        base = Base()
        self.assertEqual(base.id, 1)

    def test_id(self):
        """ testing for id of 1 """

        new_Base = Base(1)
        self.assertEqual(new_Base.id, 1)

    def test_nb_objects_id(self):
        """ Test id assigned to nb_object """

        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_id_assigned(self):
        """ test id if assigned to Base """

        base = Base(89)
        self.assertEqual(base.id, 89)

    def test_mixed_id(self):
        """ test attribute and assigned id """

        base1 = Base()
        base2 = Base(89)
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 89)
        self.assertEqual(base3.id, 2)

    def test_string_id(self):
        """ test string passed as id """

        base = Base("1")
        self.assertEqual(base.id, "1")

    def test_more_id_arguments(self):
        """ test if more than 1 arg is passed as id """
        with self.assertRaises(TypeError):
            base = Base(1, 1)

    def test_access_nb_objects(self):
        """ try access private attribute """
        base = Base()
        with self.assertRaises(AttributeError):
            base.__nb_objects

    def test_save_to_file_1(self):
        """ test JSON file """
        Square.save_to_file(None)
        result = "[]\n"
        with open("Square.json", "r") as f:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(f.read())
                self.assertEqual(str_out.getvalue(), result)

        try:
            os.remove("Square.json")
        except Exception:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_2(self):
        """ test JSON file """
        Rectangle.save_to_file(None)
        result = "[]\n"
        with open("Rectangle.json", "r") as f:
            with patch("sys.stdout", new=StringIO()) as str_out:
                print(f.read())
                self.assertEqual(str_out.getvalue(), result)

        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
