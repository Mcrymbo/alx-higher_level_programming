#!/usr/bin/python3
"""
This is a module that checks if an object is an instance of a class
specified

args:
    obj: oblect class
    instance of class to check

Return:
    True if int is and instance
    False otherwise

"""


def is_same_class(obj, a_class):
    """ check if obj is instance of a_class """

    if type(obj) is a_class:
        return True
    else:
        return False
