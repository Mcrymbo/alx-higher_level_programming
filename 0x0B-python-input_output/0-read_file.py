#!/usr/bin/python3
"""
Module that reads a text file and prints it
"""


def read_file(filename=""):
    """
    This function reads the text file

    Args:
        filename: file to open
    """

    with open(filename, encoding="utf-8") as f:
        file_read = f.read()
        print(file_read, end='')
