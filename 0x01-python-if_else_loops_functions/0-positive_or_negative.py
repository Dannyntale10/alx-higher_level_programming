#!/usr/bin/python3
import random
number = random.randint(-10, 10)

i = 1

while (i != number):
    i += 1
if (number > 0):
    print("{:d} is positive".format(number))
elif(number < 0):
    print("{:d} is negative".format(number))
elif(number == 0):
    print("{:d} is zero".format(number))  
