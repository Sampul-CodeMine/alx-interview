#!/usr/bin/env python3
"""
Module to check if the boxes can be unlocked
"""


def canUnlockAll(boxes: list) -> bool:
    """
    This is a python function that traverses through a list or list of lists
    and check if the box can be unlocked with a given key found in another box
    """

    # Check if the argument is a valid list or is not empty
    if type(boxes) is not list or len(boxes) == 0:
        return False

    keys = [0]
    for i in keys:
        for j in boxes[i]:
            if j not in keys and j != i and j < len(boxes) and j != 0:
                keys.append(j)
    if len(keys) == len(boxes):
        return True
    return False
