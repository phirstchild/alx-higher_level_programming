#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    bord (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_bord(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    bord = []
    [bord.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in bord]
    return (bord)


def bord_deepcopy(bord):
    """Return a deepcopy of a chessboard."""
    if isinstance(bord, list):
        return list(map(bord_deepcopy, bord))
    return (bord)


def get_solut(bord):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(bord)):
        for c in range(len(bord)):
            if bord[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def x_out(bord, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        bord (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(bord)):
        bord[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        bord[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(bord)):
        bord[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        bord[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(bord)):
        if c >= len(bord):
            break
        bord[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        bord[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(bord):
            break
        bord[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(bord)):
        if c < 0:
            break
        bord[r][c] = "x"
        c -= 1


def recursive_solv(bord, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        bord (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(bord):
        solutions.append(get_solution(bord))
        return (solutions)

    for c in range(len(bord)):
        if bord[row][c] == " ":
            tmp_bord = bord_deepcopy(bord)
            tmp_bord[row][c] = "Q"
            xout(tmp_bord, row, c)
            solutions = recursive_solve(tmp_bord, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    bord = init_bord(int(sys.argv[1]))
    solutions = recursive_solv(bord, 0, 0, [])
    for sol in solutions:
        print(sol)
