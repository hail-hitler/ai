def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([row.copy() for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0

def main():
    n = int(input("Enter the value of N for N-Queens: "))
    board = [[0] * n for _ in range(n)]
    solutions = []

    solve_n_queens(board, 0, n, solutions)

    print(f"\nTotal solutions for {n}-Queens: {len(solutions)}")
    for idx, sol in enumerate(solutions, start=1):
        print(f"\nSolution {idx}:")
        print_board(sol)

if __name__ == "__main__":
    main()
