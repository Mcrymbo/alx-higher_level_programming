#!/usr/bin/python3
"""
Module that implement inheritance
"""


class MyList(list):
    """ inherits from list"""

    def print_sorted(self):
        sorted_list = sorted(self.copy())
        print(sorted_list)
