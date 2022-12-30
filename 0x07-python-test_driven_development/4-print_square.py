#!/usr/bin/python3
""" prints square with character """


def print_square(size):
    """
       function that prints square with #
       Args:
           size : length of square
       Raise:
           TypeError: must be int
           ValueError: size must be >=0
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
