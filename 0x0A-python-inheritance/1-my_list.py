#!/usr/bin/python3
"""
Module that implement inheritance
"""


class MyList(list):
    """ inherits from list"""

    def print_sorted(self):
        """ prints a sorted list """

        my_list = sorted(self)
        print(my_list)
