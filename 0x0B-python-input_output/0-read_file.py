#!/usr/bin/python3
"""Module that reads a text file"""

def read_file(filename=""):
    """This is a function that reads a text file in UTF-8 and prints it to stdout"""

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")



