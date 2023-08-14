#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != len(matrix[i]) - 1:
                end_c = ' '
            else:
                end_c = ''
            print("{:d}".format(matrix[i][j]), end=end_c)
        print()
