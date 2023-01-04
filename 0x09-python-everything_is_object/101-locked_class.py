#!/usr/bin/python3
"""
class that avoids dynamically created attributes
"""


class LockedClass():
    """ locked class """
    __slots__ = ['first_name']
