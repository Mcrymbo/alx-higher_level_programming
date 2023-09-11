#!/usr/bin/python3
"""
Module that inherits from int

Args:
    int: int class

"""


class MyInt(int):
    """ inherits from class int """

    def __eq__(self, other):
        """ equal to """

        return int.__ne__(self, other)

    def __ne__(self, other):
        """ not equal to """

        return int.__eq__(self, other)
