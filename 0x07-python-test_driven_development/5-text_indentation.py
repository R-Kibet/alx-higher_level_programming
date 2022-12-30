#!/usr/bin/python3
""" prints new line after character """


def text_indentation(text):

    """
        Prints new line after . ,? :
        Args:
            text - string
        Raise:
             TypeError - text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    sp = ['.', '?', ':']
    for i in text:
        print(i, end='')
        if i in sp:
            print('\n\n', end='')
