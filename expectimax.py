import random
import copy
from getemptycells import get_empty_cells
from parameters import evaluate_board
from parameters import *
from move import *
# expectimax algorithm for 2048 game

def spawn_tile(board, pos, value):
    new_board = copy.deepcopy(board)
    new_board[pos[0]][pos[1]] = value
    return new_board

def get_valid_moves(board):
    moves = []
    for direction in ['w', 'a', 's', 'd']:
        new_board, _, moved = simulate_move(board, direction, score=0)
        if moved:
            moves.append(direction)
    return moves


def expectimax(board, depth, is_player_turn):
    if depth == 0 or not get_valid_moves(board):
        return evaluate_board(board)

    if is_player_turn:
        best_score = float('-inf')
        for move_dir in get_valid_moves(board):
            new_board, _, moved = simulate_move(board, move_dir, score=0)
            if moved:
                score = expectimax(new_board, depth - 1, False)
                best_score = max(best_score, score)
        return best_score
    else:
        empty_cells = get_empty_cells(board)
        if not empty_cells:
            return evaluate_board(board)

        expected_score = 0
        for cell in empty_cells:
            for value, prob in [(2, 0.9), (4, 0.1)]:
                new_board = spawn_tile(board, cell, value)
                score = expectimax(new_board, depth - 1, True)
                expected_score += prob * score / len(empty_cells)
        return expected_score


def find_best_move(board, depth=3):
    best_move = None
    best_score = float('-inf')
    for move_dir in get_valid_moves(board):
        new_board, _, moved = simulate_move(board, move_dir, score=0)
        if moved:
            score = expectimax(new_board, depth - 1, False)
            if score > best_score:
                best_score = score
                best_move = move_dir
    return best_move


def get_best_expectimax_move(board, invalid_moves, depth):
    best_score = float('-inf')
    best_move = None
    for move in ['w', 'a', 's', 'd']:
        new_board, score, moved = simulate_move(board, move, 0)
        if moved:
            current_score = expectimax(new_board, depth - 1, False)
            if current_score > best_score:
                best_score = current_score
                best_move = move
    return best_move

def main():
    # Initialize a 4x4 empty board
    board = [[0] * 4 for _ in range(4)]

    # Spawn two initial tiles
    for _ in range(2):
        empty = get_empty_cells(board)
        if empty:
            i, j = random.choice(empty)
            board[i][j] = random.choices([2, 4], [0.9, 0.1])[0]

    # Game loop
    while True:
        print_board(board)

        # Check if any moves are possible
        if not get_valid_moves(board):
            print("Game Over!")
            break

        # AI chooses best move using Expectimax
        move_dir = find_best_move(board, depth=3)
        if move_dir is None:
            print("No valid moves left!")
            break

        # Apply move
        new_board = simulate_move(board, move_dir)[0]
        if new_board != board:
            board = new_board

            # Spawn new tile (2 or 4)
            empty = get_empty_cells(board)
            if empty:
                i, j = random.choice(empty)
                board[i][j] = random.choices([2, 4], [0.9, 0.1])[0]
        else:
            print("Move didn't change board!")

def print_board(board):
    print("\n".join(["\t".join(map(str, row)) for row in board]))
    print()


if __name__ == "__main__":
    main()