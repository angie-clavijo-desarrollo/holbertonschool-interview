#!/usr/bin/python3

"""
Function with paramter lists of list
each lists the index[0] unlocked other box of lists
"""


def canUnlockAll(boxes):
    boxUnlocked = [0]

    for boxIndex, intoBox in enumerate(boxes):
        if not intoBox:
            continue

        for keyValue in intoBox:
            if keyValue < len(boxes) and keyValue not in boxUnlocked:
                if keyValue != boxIndex:
                    boxUnlocked.append(keyValue)

    if len(boxUnlocked) == len(boxes):
        return True
    return False
