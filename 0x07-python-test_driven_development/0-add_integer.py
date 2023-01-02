#!/usr/bin/python3

def add_integer(a, b=98):
    """A function that adds to integers.
    raises a TypeError exception if either 
    'a' or 'b' is not an integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(a, float):
        raise TypeError("b must be an integer")
    return int(a + b)
