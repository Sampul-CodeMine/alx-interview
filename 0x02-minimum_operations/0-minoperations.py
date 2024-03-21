#!/usr/bin/env python3
"""Module to perform Minimum Operation
"""
import math


def minOperations(n: int) -> int:
    """
    This is a function to get minimum operation on a string

    Args:
        n (int)
    
    Returns:
        (int) value
    """
    if type(n) is not int or n < 2:
        return 0
    ops = []
    while n % 2 == 0:
        ops.append(2)
        n /= 2
    for idx in range(3, int(math.sqrt(n)) + 1, 2):
        while n % idx == 0:
            ops.append(idx)
            n /= idx
    if n > 2:
        ops.append(n)
    operations_number = sum(ops)
    return int(operations_number)
