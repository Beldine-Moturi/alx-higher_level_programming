#!/usr/bin/python3
def uppercase(str):
    """
    prints a string in uppercase
    """
    my_string = ""
    for char in str:
        if ord(char) in range(97, 123):
            my_string = my_string + '{:c}'.format(ord(char) - 32)
        else:
            my_string = my_string + '{}'.format(char)
    print('{:s}'.format(my_string))
