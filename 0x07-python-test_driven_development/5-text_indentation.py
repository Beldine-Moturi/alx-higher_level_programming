#!/usr/bin/python3
"""
This module describes one function ``text_indentation()``
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): the text to be printed
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    new_text = text.split()
    for i in range(len(new_text)):
        if ('.' in new_text[i] or
                '?' in new_text[i] or
                ':' in new_text[i]):
            for char in new_text[i]:
                if char in ['.', '?', ':']:
                    print(char)
                    print()
                else:
                    print(char, end='')
        elif i != (len(new_text) - 1):
            print(new_text[i], end=' ')
        else:
            print(new_text[i], end='')
