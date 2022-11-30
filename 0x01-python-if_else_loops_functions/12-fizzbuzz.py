#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num == 3:
            print("Fizz")
        elif num == 5:
            print("Bizz")
        elif num == 3 and 5:
            print("fizzbuzz")
        else:
            print("{}".format(num), end="")
