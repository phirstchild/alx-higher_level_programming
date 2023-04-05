#!/usr/bin/python3
"""Solves the N-queens puzzle.

This program will determine available position for
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N is an integer greater than or equal to 4.

Attributes:
    chess_board (list): A list of lists representing the chessboard.
    board_solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    chess_board = []
    [chess_board.append([]) for item in range(n)]
    [row.append(' ') for item in range(n) for row in chess_board]
    return (chess_board)


def board_deepcopy(chess_board):
    """Return a deepcopy of a chessboard."""
    if isinstance(chess_board, list):
        return list(map(board_deepcopy, chess_board))
    return (chess_board)


def get_solution(chess_board):
    """Return the list of lists representation of a solved chessboard."""
    board_solution = []
    for r in range(len(chess_board)):
        for c in range(len(chess_board)):
            if chess_board[r][c] == "Q":
                board_solution.append([r, c])
                break
    return (board_solution)


def xout(chess_board, row, col):
    """All spots where non-attacking queens can no
    longer be played are masked out with X

    Args:
        chess_board (list): my current chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(chess_board)):
        chess_board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        chess_board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(chess_board)):
        chess_board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        chess_board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(chess_board)):
        if c >= len(chess_board):
            break
        chess_board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chess_board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chess_board):
            break
        chess_board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(chess_board)):
        if c < 0:
            break
        chess_board[r][c] = "x"
        c -= 1


def recursive_solve(chess_board, row, queens, chess_solutions):
    """Recursively solvely the N-queens puzzle.

    Args:
        chess_board (list): My current working chessboard.
        row (int): My current row.
        queens (int): My current number of placed queens.
        chess_solutions (list): My list of lists of solutions.
    Returns:
        chess_solutions
    """
    if queens == len(chess_board):
        chess_solutions.append(get_solution(chess_board))
        return (chess_solutions)

    for c in range(len(chess_board)):
        if chess_board[row][c] == " ":
            temp_board = board_deepcopy(chess_board)
            temp_board[row][c] = "Q"
            xout(temp_board, row, c)
            chess_solutions = recursive_solve(temp_board, row + 1,
                                        queens + 1, chess_solutions)

    return (chess_solutions)


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

    chess_board = init_board(int(sys.argv[1]))
    chess_solutions = recursive_solve(chess_board, 0, 0, [])
    for result in chess_solutions:
        print(result)
