#!/usr/bin/python3
"""
Module that creates object fron json file
"""
import json


def load_from_json_file(filename):
    """
    function to create an object fie

    Args:
        filename: file
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
