#!/usr/bin/python3
""" inheritance directly or indirectly """


def inherits_from(obj, a_class):
    """ class inherited directly or indirectly """

    if type(obj) != a_class:
        return isinstance(obj, a_class)
    return False
