#!/usr/bin/python3
def remove_char_at(str, n):
    my_string = ""
    for i, v in enumerate(str):
        if i == n:
            continue
        else:
            my_string += str[i]
    return my_string
