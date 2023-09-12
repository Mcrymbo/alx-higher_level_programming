#!/usr/bin/python3
"""
A module that appends atring to a text file
"""


def append_write(filename="", text=""):
    """
    A function that appends string

    Args:
        filename: name of file. create if it doesn't exist
        text: string to add

    Return: Number of string appended
    """

    with open(filename, "a+", encoding='utf-8') as f:
        return f.write(text)
