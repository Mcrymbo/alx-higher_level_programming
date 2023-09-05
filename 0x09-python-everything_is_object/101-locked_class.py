#!/usr/bin/python3
""" class that allonly addintion of only first_name
as the instance variable and voids the rest"""


class LockedClass:
    __slots__ = ["first_name"]
