#!/usr/bin/python3

"""A module that checks if an object is exactly
    an instance of a specific class.
"""

def is_same_class(obj, a_class):
    """Returns True if the object is exactly an
        instance of the specific class;
        otherwise False.
    """
    if type(obj) is a_class:
        return True
    return False
