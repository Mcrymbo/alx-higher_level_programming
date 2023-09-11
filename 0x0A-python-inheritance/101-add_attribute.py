#!/usr/bin/python3
"""
Module to add a new attribute to an object
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to object

    Args:
        obj: object in which attribute is to be added
        name: attribute name
        value: value to assign to attribute name

    Raises:
        TypeError: raised if object can't have new attribute

    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
