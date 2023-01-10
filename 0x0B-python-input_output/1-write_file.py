#!/usr/bin/python3
"""Module that writes astring to a text file"""

def write_file(filename="", text=""):
    """A function that writes a string to a tex tfile(UTF8) and
        returns the number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
