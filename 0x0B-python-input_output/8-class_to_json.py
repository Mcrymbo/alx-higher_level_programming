#!/usr/bin/python3
"""
Module that rturns dictionary description
"""


def class_to_json(obj):
    """
    a function that returns dictionary description
    
    Args:
        obj: instance of a class
    """

    dict_des = {}
    if hasattr(obj, "__dict__"):
        dict_des = obj.__dict__.copy()
    return dict_des
