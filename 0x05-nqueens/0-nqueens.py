#!/usr/bin/python3
"""Solving N Queens"""
import sys


def nqueens(n, y, board):
    """
        Usage: nqueens N
        If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
        where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
        If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
    """
    for x in range(n):
        hold = 0
        for q in board:
            if x == q[1]:
                hold = 1
                break
            if y - x == q[0] - q[1]:
                hold = 1
                break
            if x - q[1] == q[0] - y:
                hold = 1
                break
        if hold == 0:
            board.append([y, x])
            if y != n - 1:
                nqueens(n, y + 1, board)
            else:
                print(board)
            del board[-1]


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n, 0, [])


if __name__ == '__main__':
    main()
