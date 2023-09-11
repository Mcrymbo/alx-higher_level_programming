#!/usr/bin/python3
"""
Module to check if object is an instance that inherited from a specified
class

Args:
    obj: object
    a_class: class

Return:
    True if isinstance
"""


def inherits_from(obj, a_class):
    """ function to implement the module """

    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
