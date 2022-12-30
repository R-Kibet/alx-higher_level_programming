#!/usr/bin/python3
""" divides all elements ina matrix """


def matrix_divided(matrix, div):

    """ Divides elements of a matrix
    Args:
       matrix: list of matrix
       div: the divisor

    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if all(type(i) not in [int, float] for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    new = [[eval("{:.2f}".format(i / div)) for i in row] for row in matrix]

    return new
