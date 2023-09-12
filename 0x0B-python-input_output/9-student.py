#!/usr/bin/python3
"""
class module that defines a student
"""


class Student:
    """ class that defines student details """

    def __init__(self, first_name, last_name, age):
        """ initializes instance attributes """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation """

        return self.__dict__.copy()
