#!/usr/bin/python3
""" Function that prints full name"""


def say_my_name(first_name, last_name=""):
    """
      Function that prints first and last name

    Args:
        First_name: first name
        last_name: last name
    Raises:
        TypeError: if names not string:
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
