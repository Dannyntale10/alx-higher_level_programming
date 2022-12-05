#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = tuple(map(sum,zip(tuple_a, tuple_b)))
    return new_tuple
    if new_tuple < 2:
        return 0
    elif new_tuple > 2:
        return new_tuple[0:2]
