#!/usr/bin/python3
"""  inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file """
    with open(filename, "r+") as f:
        s = f.readlines()
        c = []

        for i in range(len(s)):
            c.append(s[i])
            if search_string in s[i]:
                c.append(new_string)

        f.seek(0)
        f.write("".join(c))
