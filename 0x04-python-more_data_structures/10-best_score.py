#!/usr/bin/python3
def best_score(a_dictionary):
    """return key with biggest int value"""
    if a_dictionary is None:
        return None
    my_list = sorted(list(a_dictionary.values()))
    return (my_list[len(my_list) - 1])
