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
    if type(boxes) == list or len(boxes) > 0:
        for idx in range(1, len(boxes) - 1):
            checked_box = False
            for i in range(len(boxes)):
                checked_box = (idx in boxes[i] and idx != i)
                if checked_box is True:
                    break
            if not checked_box:
                return checked_box
        return True
    return False
