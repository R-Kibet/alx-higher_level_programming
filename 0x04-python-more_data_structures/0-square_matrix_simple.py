#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new = []
    for i in matrix:
        result = list(map(lambda x: x**2, i))
        new.append(result)
    return new
