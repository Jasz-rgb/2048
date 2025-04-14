import random

def create_board():
    """
    Creates a 4x4 board (2D list) initialized with all values set to 0.
    """
    board = [[0 , 0 , 0 , 0 ] for _ in range(4)]
    return board

def generate_initial_tiles(board):
    """
    Generates two initial tiles (2 or 4) on the board.
    Cell 2 appearance probability: 90%
    Cell 4 appearance probability: 10%
    """
    board = generate_new_tile(board)
    board = generate_new_tile(board)

    return board

def generate_new_tile(board):
    """
    Generates a new tile (2 or 4) at a random empty position on the board.
    Cell 2 appearance probability: 90%
    Cell 4 appearance probability: 10%
    """
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        if random.random() < 0.9:  # 90% probability of generating 2
            board[i][j] = 2
        else:  # 10% probability of generating 4
            board[i][j] = 4
    return board