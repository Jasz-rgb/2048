# --- Parameters & evaluation function ---

def count_empty_cells(board):
    """
    Counts the number of empty cells in the board without using NumPy.
    """
    count = 0
    for row in board:
        for cell in row:
            if cell == 0:
                count += 1
    return count

def calculate_monotonicity(board):
    """
    Evaluates the monotonicity of the board by checking if tiles are generally arranged in ascending or descending order.
    """
    monotonicity_score = 0
    for i in range(4):
        # Check rows
        row = board[i]
        sorted_row = sorted(row)
        if row == sorted_row or row == sorted_row[::-1]:
            monotonicity_score += 1  # Row is monotonic
        
        # Check columns
        col = [board[j][i] for j in range(4)]
        sorted_col = sorted(col)
        if col == sorted_col or col == sorted_col[::-1]:
            monotonicity_score += 1  # Column is monotonic
    
    return monotonicity_score

def calculate_smoothness(board):
    """
    Calculates the smoothness of the board by penalizing large differences between adjacent tiles.
    """
    smoothness_score = 0
    for i in range(4):
        for j in range(3):  # Check adjacent tiles in the row
            row_diff = abs(board[i][j] - board[i][j+1])
            smoothness_score -= row_diff  # Lower differences are better
        for j in range(3):  # Check adjacent tiles in the column
            col_diff = abs(board[j][i] - board[j+1][i])
            smoothness_score -= col_diff  # Lower differences are better
    
    return smoothness_score


def check_highest_tile_in_corner(board):
    max_tile = max(max(row) for row in board)
    return 1 if board[3][0] == max_tile else 0  # Checks if the highest tile is in the bottom left corner

def evaluate_board(board):

    empty = count_empty_cells(board)
    mono = calculate_monotonicity(board)
    smooth = calculate_smoothness(board)
    corner_bonus = check_highest_tile_in_corner(board)

    return (
        empty * 2.7 +
        mono * 1.0 +
        smooth * 0.1 +
        corner_bonus * 1000  # big bonus if max tile is in the bottom left corner
    )