#!/usr/bin/python3
"""
module that implements pascal triangle
"""


def pascal_triangle(n):
    """
    Function that returns pascal triangle n

    Args:
        n: number of lines12-pascal_triangle.py 12-pascal_triangle.py

    Return:
        matrix with pascal triangle
    """

    matrix = []
    res = []
    for i in range(n):
        list_res = []
        p1 = -1
        p2 = 0
        for j in range(len(res) + 1):
            if p1 == -1 or p2 == len(res):
                list_res += [1]
            else:
                list_res += [res[p1] + res[p2]]
            p1 += 1
            p2 += 1
        matrix.append(list_res)
        res = list_res[:]
    return matrix
