
def is_game_over(board):
    # (function to check if there are no more moves)
    # Checks for empty cells and possible merges
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False  # Empty cell exists, game is not over
            if i < 3 and board[i][j] == board[i+1][j]:
                return False  # Can merge down
            if j < 3 and board[i][j] == board[i][j+1]:
                return False  # Can merge right
    return True  # No moves left, game over


def has_won(board):
    for row in board:
        if 2048 in row:
            return True
    return False