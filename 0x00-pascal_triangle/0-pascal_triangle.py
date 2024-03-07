#!/usr/bin/python3
"""
This is a module to carry out getting the coefficient of a value
using Pascal's Triangel
"""


def pascal_triangle(n: int) -> list:
    """
    This is a function that returns a list of lists of integers
    representing all the co-efficients of n using Pascal's triangle.

    Args:
        n (int): value to find its coefficient

    Returns:
        list: list of lists of integers with resulting coefficients
    """

    t_angle = []
    if type(n) is not int or n <= 0:
        return t_angle
    for itr1 in range(n):
        tmp_row = [1 if j == 0 or j == itr1 else (t_angle[itr1 - 1][j - 1] +
                                                  t_angle[itr1 - 1][j])
                   for j in range(itr1 + 1)]
        t_angle.append(tmp_row)
    return t_angle
