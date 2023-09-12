#!/usr/bin/python3
"""
module that writes an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an object to tesxt file

    Args:
        my_obj: python object
        filename: file to write text object to

    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
