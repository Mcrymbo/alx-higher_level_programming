#!/usr/bin/python3
"""
module that finds a peak in unsorted integers
"""


def find_peak(list_of_integers):
    """ modules that finds a peak/max in integers """

    if not list_of_integers:
        return None

    lis = list_of_integers
    length = len(lis)
    mid = int(length / 2)

    if mid - 1 < 0 and mid + 1 >= length:
        return lis[mid]
    elif mid - 1 < 0:
        if lis[mid] > lis[mid + 1]:
            return lis[mid]
        else:
            return lis[mid + 1]
    elif mid + 1 >= length:
        if lis[mid] > lis[mid - 1]:
            return lis[mid]
        else:
            return lis[mid - 1]
    if lis[mid - 1] < lis[mid] > lis[mid + 1]:
        return lis[mid]
    if lis[mid + 1] > lis[mid - 1]:
        return find_peak(lis[mid:])
    return find_peak(lis[:mid])
