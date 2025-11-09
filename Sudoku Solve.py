print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO SOLVE A GIVEN 9X9 SUDOKU")
print()
# Sudoku Solver using Backtracking

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None


def is_valid(board, num, pos):
    row, col = pos

    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve(board):
    find = find_empty(board)
    if not find:
        return True  # Solved
    row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Example Sudoku puzzle (0 = empty cell)
sudoku_board = [
    [0, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 4, 0, 0, 8, 6, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 3, 2],
    [0, 0, 6, 0, 9, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 5, 3],
    [0, 0, 0, 5, 3, 0, 6, 2, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 5, 4, 2, 0, 0, 6, 0],
    [0, 0, 1, 8, 7, 0, 0, 0, 5]
]

print("Original Sudoku:")
print_board(sudoku_board)
solve(sudoku_board)
print("\nSolved Sudoku:")
print_board(sudoku_board)
