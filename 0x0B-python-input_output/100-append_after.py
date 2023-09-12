#!/usr/bin/python3
"""
Module of a function that inserts a line of text
"""


def append_after(filename="", search_string='', new_string=''):
    """
    Function that inserts a new line to a text file

    Args:
        filename: name of the file
        search_string: string being searched
        new_string: string being appended
    """

    lines = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            lines += [line]
            if line.find(search_string) != -1:
                lines += [new_string]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(''.join(lines))
