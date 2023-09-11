#!/usr/bin/python3
"""
Module that checks if an object is an instance of or in ainstance
of a class that it inherited from

Args:
    obj: object
    a_class: instance

Return:
    True if it is an instance
    False: otherwise

"""


def is_kind_of_class(obj, a_class):
    """ check if isinstance of a class """

    if isinstance(obj, a_class):
        return True
    else:
        return False
