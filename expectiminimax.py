from ai import simulate_move
from checkwin import is_game_over
from getemptycells import get_empty_cells, place_tile
from parameters import count_empty_cells, calculate_monotonicity, calculate_smoothness, check_highest_tile_in_corner
#expectiminimax algorithm for 2048 game

INF = 2**64
PERFECT_SNAKE = [[2,   2**2,  2**3,  2**4],
                [2**8, 2**7,  2**6,  2**5],
                [2**9, 2**10, 2**11, 2**12],
                [2**16, 2**15, 2**14, 2**13]]
"""Perfect Snake algorithm for 2048 game as a parameter."""

def snakeHeuristic(board):
    score = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                continue
            score += (PERFECT_SNAKE[i][j] * board[i][j]) * 10
    score += count_empty_cells(board) * 2
    score += check_highest_tile_in_corner(board) * 5
    return score

def getNextBestMoveExpectiminimax(board):
    depth = 4
    best_move = None
    best_score = -INF

    for move in ['w', 'a', 's', 'd']:
        new_board, _, moved = simulate_move(board, move, score=0)
        if moved:
            eval_score, _ = expectiminimax(new_board, depth - 0.5, False)
            if eval_score > best_score:
                best_score = eval_score
                best_move = move

    if best_move is None:
        print("No valid moves available.")
        return None

    print(f"Best move found: {best_move} with score: {best_score}")
    return best_move

def expectiminimax(board, depth, is_maximizing_player):
    if depth <= 0 or is_game_over(board):
        return snakeHeuristic(board), None

    if is_maximizing_player:
        best_score = -INF
        best_move = None
        for move in ['w', 'a', 's', 'd']:
            new_board, _, moved = simulate_move(board, move, score=0)
            if moved:
                eval_score, _ = expectiminimax(new_board, depth - 0.5, False)
                if eval_score > best_score:
                    best_score = eval_score
                    best_move = move
        return best_score, best_move

    else:
        empty_cells = get_empty_cells(board)
        if not empty_cells:
            return snakeHeuristic(board), None

        expected_score = 0
        for position in empty_cells:
            for tile_value, probability in [(2, 0.9), (4, 0.1)]:
                new_board = place_tile(board, position, tile_value)
                eval_score, _ = expectiminimax(new_board, depth - 1, True)
                expected_score += probability * eval_score
        expected_score /= len(empty_cells)
        return expected_score, None
