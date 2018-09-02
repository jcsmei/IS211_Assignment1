#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple assingment1_part1"""


def listDivide(numbers, divide=2):
    """Divdes the number of elements in the list of numbers that are divisible
        by divide.

        Arg:
            numbers (list): a list of integers
            divide (int): an intetger       Default: 2

        Returns:
            int: The integer divisible by divide

        Exmaples:
            >>> listDivide([1,2,3,4,5])
            2
            >>> listDivide([2, 4, 6, 8, 10])
            5
            >>> listDivide([30, 54, 63, 98, 100], 10)
            2
        """
    i = 0
    for item in numbers:
            if item % divide == 0:
                i += 1
    return i


class ListDivideException(Exception):
        """List Divide exception class."""
        pass


def testListDivide():
    """A function to test ListDivide."""
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException("List Divide Exception")
    elif listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException("List Divide Exception")
    elif listDivide([30, 54, 63, 98, 100], 10) != 2:
        raise ListDivideException("List Divide Exception")
    elif listDivide([]) != 0:
        raise ListDivideException("List Divide Exception")
    elif listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException("List Divide Exception")
        

if __name__ ==  "__main__":
    testListDivide()
