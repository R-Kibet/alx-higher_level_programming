#!/usr/bin/python3
""" function that reads a text file (UTF8)"""


def read_file(filename=""):
    """ eads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")