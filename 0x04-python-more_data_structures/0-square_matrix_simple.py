#!/usr/bin/python3
"""
Function to compute the square value of all integers in a matrix
"""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with the square values"""
    new_matrix = [list(map(lambda x: x**2, row)) for row in matrix]
    return new_matrix


