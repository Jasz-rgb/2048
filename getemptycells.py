def get_empty_cells(board):
    empty_cells = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells

def place_tile(board, position, value):
    new_board = [row[:] for row in board]
    new_board[position[0]][position[1]] = value
    return new_board
