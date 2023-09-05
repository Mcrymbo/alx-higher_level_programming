#!/usr/bin/python3
""" class that allonly addintion of only first_name
as the instance variable and voids the rest"""


class LockedClass:
    """ class that voids other instance attributes """

    __slots__ = ["first_name"]
