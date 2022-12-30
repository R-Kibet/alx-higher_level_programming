#!/usr/bin/python3
""" Function that add integers """


def add_integer(a, b=98):
    """ addition of two ints
    Args :
        a - first int
        b - second int
    return :
        addtion of 2 ints
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
