#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """delete a key in a dict"""
    a_dictionary.pop(key, None)
    return a_dictionary
