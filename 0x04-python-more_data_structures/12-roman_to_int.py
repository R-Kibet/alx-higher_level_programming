#!/usr/bin/python3

def roman_to_int(roman_string):

    # CREATE A DICTIONARY
    m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    n = len(roman_string)
    i = n - 1
    out = 0
    if roman_string:
        while i >= 0:
            if i < n - 1 and m[roman_string[i]] < m[roman_string[i + 1]]:
                out -= m[roman_string[i]]
            else:
                out += m[roman_string[i]]
            i -= 1
    else:
        return 0
    return out
