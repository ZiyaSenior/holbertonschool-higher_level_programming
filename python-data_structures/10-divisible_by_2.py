#!/usr/bin/python3

# function that returns a list of True/False for multiples of 2
def divisible_by_2(my_list=[]):
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result  
