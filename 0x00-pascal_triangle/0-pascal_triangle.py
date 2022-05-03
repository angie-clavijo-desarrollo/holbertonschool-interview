#!/usr/bin/python3
"""
Pascals
"""


def pascal_triangle(n):
    """
    def pascal_triangle(n):
    that returns a list of lists of integers representing
    the Pascal’s triangle of n:
    """
    list = []
    if n > 0:
        for i in range(n):
            list.append([])
            list[i].append(1)
            for j in range(1, i):
                list[i].append(list[i - 1][j - 1] + list[i - 1][j])
            if i != 0:
                list[i].append(1)

    return list
