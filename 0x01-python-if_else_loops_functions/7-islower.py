#!/usr/bin/python3
def islower(c):
    """
    Checks for a lowercase character

    Returns true if found, False otherwise
    """
    ascii_val = ord(c)
    if ascii_val in range(97, 123):
        return True
    else:
        return False
