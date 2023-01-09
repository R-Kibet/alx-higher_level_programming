#!/usr/bin/python3
""" object instance of a class """


def is_same_class(obj, a_class):
    """ a funcrion that return true or false

        Args:
            obj - object
            a_class- class
    """

    return type(obj) == a_class
