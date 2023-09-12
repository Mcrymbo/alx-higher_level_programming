#!/usr/bin/python3
"""
module that handles JSON representation of an object
"""
import json

def to_json_string(my_obj):
    """
    Function that serializes a python object

    Args:
        my_object: python object or dictionary

    Return:
        JSON object
    """

    return json.dumps(my_obj)
