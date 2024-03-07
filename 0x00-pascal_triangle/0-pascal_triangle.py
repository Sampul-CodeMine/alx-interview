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

    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        tr = [1 if j == 0 or j == i else (triangle[i - 1][j - 1] +
                                          triangle[i - 1][j])
              for j in range(i + 1)]
        triangle.append(tr)
    return triangle
