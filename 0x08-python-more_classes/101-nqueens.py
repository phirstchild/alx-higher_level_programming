#!/usr/bin/python3

import sys

# Define function to check if a given position is safe for a queen
def Safeif(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

# Define function to solve N queens problem
def solveQueensN(N):
    board = [[0 for x in range(N)] for y in range(N)]
    solveQueensNUtil(board, 0, N)

# Define recursive function to solve N queens problem
def solveQueensNUtil(board, row, N):
    # Base case: all queens have been placed
    if row == N:
        printBoard(board)
        return True

    # Try placing queen in each column of current row
    for col in range(N):
        if Safeif(board, row, col, N):
            board[row][col] = 1
            solveQueensNUtil(board, row+1, N)
            board[row][col] = 0

    return False

# Define function to print the board
def prntBoard(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
    print()

# Parse command line argument
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Solve N queens problem
solveQueensN(N)
