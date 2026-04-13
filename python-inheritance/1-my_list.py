#!/usr/bin/python3
"""
Module Name: 1-my_list

Module Description:
This module contains only one function

Module Classes:
- MyList

Module Attributes:
- None
"""


class MyList(list):
    """
    A subclass of the built-in list class that provides an additional
    method for printing the list in sorted order.
    """
    def print_sorted(self):
        """
        Sort the list in ascending order and print it to the console.
        """
        print(sorted(self))
