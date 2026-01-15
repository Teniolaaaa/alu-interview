#!/usr/bin/python3
"""
Module for calculating minimum operations needed to get n H characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.

    Starting with 1 H, the only operations allowed are:
    - Copy All: copies all characters currently in the file
    - Paste: pastes the copied characters

    Args:
        n: target number of H characters

    Returns:
        Integer representing minimum number of operations needed
        Returns 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Find all prime factors and sum them
    # The minimum operations = sum of all prime factors (with multiplicity)
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
