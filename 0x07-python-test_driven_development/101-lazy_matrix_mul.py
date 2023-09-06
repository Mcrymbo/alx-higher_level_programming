#!/usr/bin/python3
""" This module used to calculate two matrices using numpy module """

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ function that multiply 2 matrices using numpy module """

    return (np.matmul(m_a, m_b))
