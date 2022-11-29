#!/usr/bin/python3
import random
number = random.randint(-10, 10)

i = 1

while (i != number):
    i += 1
if (number > 0):
    print("{} is positive".format(number))
elif(number < 0):
    print("{} is negative".format(number))
elif(number == 0):
    print("{} is zero".format(number))  
