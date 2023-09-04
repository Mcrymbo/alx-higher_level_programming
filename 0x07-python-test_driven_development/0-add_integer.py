#!/usr/bin/python3


def add_integer(a, b=98):
    """ adds two numbers that are either int or float """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
