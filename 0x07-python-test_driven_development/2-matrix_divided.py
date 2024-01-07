#!/usr/bin/python3
"""
Module for matrix division.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Parameters:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide the matrix by.

    Returns:
        list: A new matrix with all elements divided by div (rounded to 2 decimal places).

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if type(matrix) is not list or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
