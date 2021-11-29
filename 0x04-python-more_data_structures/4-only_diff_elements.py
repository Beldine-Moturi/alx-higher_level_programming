#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """return set of elements only present in one set"""
    return (set_1 ^ set_2)
