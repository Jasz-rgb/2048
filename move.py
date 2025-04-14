
# --- Game Movement Functions & simulation function ---

def move_up(board, score):
    """
    Moves cells up, merging similar cells.
    Returns the new board and a boolean indicating if the move changed the board or if it was a null move.
    """
    moved = 0   # initialising moved to false
    original_board = [row[:] for row in board]  # Create a DEEP COPY of the board 
    board = [list(col) for col in zip(*board)]  # now board is a nested list of columns instead of rows to acess each column for move_up function
    
    for i in range(4):  # Iterates through each column
        column = [cell for cell in board[i] if cell != 0]       # Remove zeros (empty cells)
        
        # Merge similar cells
        merged_column = []                       # empty column
        index = 0                                    # taken an index i for cells, starting from first cell (index, i = 0)
        while index < len(column):
            if index + 1 < len(column) and column[index] == column[index + 1]:  # if consecutive cells found same then add them
                merged_column.append(column[index] * 2)
                score += column[index] * 2
                index += 2                           # next go to 2 index later 
                moved = 1                       # Board is changed
            else:
                merged_column.append(column[index])
                index += 1                           # if next cell not same, then go to next cell
        
        while len(merged_column) < 4:
            merged_column.append(0)              # add zeroes to left over cells
        
        board[i] = merged_column                 # Update the column in the board
    
    board = [list(row) for row in zip(*board)]   # Transpose the board back to its original orientation
    
    if original_board != board:
        moved = 1                                # Set 'moved' 1 if the board changed at all

    return board, score, moved

def move_down(board, score):
    """
    Moves cells down, merging similar cells.
    Returns the new board and a boolean indicating if the move changed the board.
    """
    moved = 0
    original_board = [row[:] for row in board]
    board = [list(col) for col in zip(*board)]
    
    for i in range(4):
        column = [cell for cell in board[i] if cell != 0]
        
        merged_column = []
        index = len(column) - 1
        while index >= 0:
            if index > 0 and column[index] == column[index - 1]:
                merged_column.insert(0, column[index] * 2)
                score += column[index] * 2
                index -= 2
                moved = 1
            else:
                merged_column.insert(0, column[index])
                index -= 1
        
        while len(merged_column) < 4:
            merged_column.insert(0, 0)
        
        board[i] = merged_column
    
    board = [list(row) for row in zip(*board)]

    if original_board != board:
        moved = 1
    
    return board, score, moved


def move_left(board, score):
    """
    Moves cells left, merging similar cells.
    Returns the new board and a boolean indicating if the move changed the board.
    """
    moved = 0
    original_board = [row[:] for row in board]  # Creates a DEEP COPY of the board 
    for i in range(4):  # Iterate through each row
        # Removes zeros (empty cells)
        row = [cell for cell in board[i] if cell != 0]
        
        # Merges similar cells
        merged_row = []
        index = 0
        while index < len(row):
            if index + 1 < len(row) and row[index] == row[index + 1]:
                merged_row.append(row[index] * 2)
                score += row[index] * 2
                index += 2
            else:
                merged_row.append(row[index])
                index += 1
        
        # Adds zeros back to fill the row
        while len(merged_row) < 4:
            merged_row.append(0)
        
        # Updates the row in the board
        board[i] = merged_row
    
    if original_board != board:
        moved = 1                                # Sets 'moved' 1 if the board changed at all

    return board, score, moved


def move_right(board, score):
    """
    Moves cells right, merging similar cells.
    Returns the new board and a boolean indicating if the move changed the board.
    """
    moved = 0
    original_board = [row[:] for row in board]
    for i in range(4):
        row = [cell for cell in board[i] if cell != 0]
        
        merged_row = []
        index = len(row) - 1
        while index >= 0:
            if index > 0 and row[index] == row[index - 1]:
                merged_row.insert(0, row[index] * 2)
                score += row[index] * 2
                index -= 2
            else:
                merged_row.insert(0, row[index])
                index -= 1
        
        while len(merged_row) < 4:
            merged_row.insert(0, 0)
        
        board[i] = merged_row
    
    if original_board != board:
        moved = 1
    
    return board, score, moved

def simulate_move(board, move, score):
    new_board = [row[:] for row in board]  # Creates a copy of the board
    
    if move == 'w':
        new_board, score, moved = move_up(new_board, score)
    elif move == 'a':
        new_board, score, moved = move_left(new_board, score)
    elif move == 's':
        new_board, score, moved = move_down(new_board, score)
    elif move == 'd':
        new_board, score, moved = move_right(new_board, score)
    else:
        moved = False  # fallback if invalid move
    
    return new_board, score, moved

