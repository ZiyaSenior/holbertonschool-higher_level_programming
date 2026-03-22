#!/usr/bin/python3

# import functions from calculator_1.py only once
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    results = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    operations = ["+", "-", "*", "/"]

    for op, res in zip(operations, results):
        print("{} {} {} = {}".format(a, op, b, res))
