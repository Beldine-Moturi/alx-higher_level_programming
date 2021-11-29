#!/usr/bin/python3
def best_score(a_dictionary):
    """return key with biggest int value"""
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    key = list(a_dictionary.keys())[0]
    val = a_dictionary[key]
    for i, j in a_dictionary.items():
        if j > val:
            key = i
            val = j
    return key
