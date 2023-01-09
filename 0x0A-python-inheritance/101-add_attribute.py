#!/usr/bin/python3
"""
function that add new attribute to an object
"""


def add_attribute(obj, name, value):
    """Function  """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
