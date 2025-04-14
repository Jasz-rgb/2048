
def print_board(board):
    for row in board:
        print("   ".join(str(x) if x != 0 else '.' for x in row))
    print()