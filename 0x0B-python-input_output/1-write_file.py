#!/usr/bin/python3

"""
Module for writing a string to a text file
"""


def write_file(filename='', text=''):
    """
    A function that writes a string to text file

    Args:
        filename: a file to write data into
        text: text data to add to file

    """

    with open(filename, mode='w', encoding='utf-8') as f:
       return f.write(text)
