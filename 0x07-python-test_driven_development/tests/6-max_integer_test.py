#!/usr/bin/python3
""" unitests for testing maximum integer """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestmaxInteger(unittest.TestCase):
    """ used to test for max integer """

    def test_max_integer(self):
        self.assertEqual(max_integer([4, 50, -10, 30]), 50)

    def test_repeated_number(self):
        self.assertEqual(max_integer([20, 20, 20, 20]), 20)

    def test_max_at_beggining(self):
        self.assertEqual(max_integer([7, 3, 2, 1]), 7)

    def test_float_number(self):
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_loop(self):
        lst = [1, 3, 5, 7, 5, 2]
        self.assertEqual(max_integer([i ** 2 for i in lst]), 49)

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_list_with_one_number(self):
        self.assertEqual(max_integer([2]), 2)

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 3, 'key2': 7})

    def test_tuple(self):
        with self.assertRaises(TypeError):
            max_integer([1, (1, 2)])

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, '2'])
