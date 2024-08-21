#!/usr/bin/python3
"""
This module contains the minOperations function.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed
    to get exactly n 'H' characters in the file.

    :param n: The target number of 'H' characters.
    :return: The minimum number of operations or 0
    if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
