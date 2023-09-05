#!/usr/bin/python3
""" class LockedClass
    (prevents the user from dynamically creating new instance)
"""


class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self):
        """ initializes instance attributes """
