#!/usr/bin/python3
"""
Module that returns object
"""
import json


def from_json_string(my_str):
    """
    Function that returns JSON string

    Args:
        my_str: json string

    Return:
        python object
    """

    return json.loads(my_str)
