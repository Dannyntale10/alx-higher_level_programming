#!/usr/bin/python3
def max_integer(my_list=[]):

    big_number = my_list[0]

    for number in my_list:
        if number > big_number:
            big_number = number
            return big_number
        for numbers in my_list:
            if my_list == "":
                return None
