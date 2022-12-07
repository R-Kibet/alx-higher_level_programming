#!/usr/bin/pyhton3

def best_score(a_dictionary):
    if a_dictionary:
        s = max(a_dictionary, key=a_dictionary.get)
    else:
        return None
    return s
