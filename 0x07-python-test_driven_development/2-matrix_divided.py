#!/usr/bin/python3


def matrix_divided(matrix, div):
    """ method that divides all the elements of a matrix """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row_matrix = []
        for i in row:
            result = round(i / div, 2)
            row_matrix.append(result)
        new_matrix.append(row_matrix)
    return new_matrix
