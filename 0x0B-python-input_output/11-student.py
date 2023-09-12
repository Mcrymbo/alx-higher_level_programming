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

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation """

        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj
            res = {}
            for i in range(len(attrs)):
                for j in obj:
                    if attrs[i] == j:
                        res[j] = obj[j]
            return res
        return obj

    def reload_from_json(self, json):
        """ replaces all attributes of a student """

        for i in json:
            self.__dict__[i] = json[i]
