def is_safe(board, row, col, n):
    """Check if a queen can be placed safely at board[row][col]"""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(n, row=0, board=[]):
    """Recursive function to solve N-Queens using backtracking"""
    if row == n:
        print_solution(board, n)
        return True  # Return True to find only one solution
    for col in range(n):
        if is_safe(board, row, col, n):
            solve_n_queens(n, row + 1, board + [col])

def print_solution(board, n):
    """Print the board with emojis for better visualization"""
    print("\nSolution:")
    for row in range(n):
        line = ["♛" if board[row] == col else "." for col in range(n)]
        print(" ".join(line))
    print("=" * (2 * n - 1))  # Separator for clarity

# Run for 8-Queens (change N for different sizes)
N = 8
solve_n_queens(N)
