#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first = ""
    if sentence == "":
        first = "None"
    for i in range(0, 1):
        first = first + sentence[i]
    return (length, first)
