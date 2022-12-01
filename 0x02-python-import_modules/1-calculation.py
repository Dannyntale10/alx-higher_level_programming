#!/usr/bin/python3
if __name__ == "__main__":

    a = 10
    b = 5

    from calculator_1 import add
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

    from calculator_1 import sub
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))

    from calculator_1 import mul
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))

    from calculator_1 import div
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

