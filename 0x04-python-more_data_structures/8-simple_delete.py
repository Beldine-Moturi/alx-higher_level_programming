#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """delete a key in a dict"""
    del a_dictionary[key]
    return a_dictionary
