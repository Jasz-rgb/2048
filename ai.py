from move import simulate_move
from parameters import evaluate_board

def evaluate_all_moves(board, invalid_moves, current_score):
    best_move = None
    best_score = float('-inf')

    possible_moves = ['w', 'a', 's', 'd']
    for move in possible_moves:
        if move in invalid_moves:
            continue

        simulated_board, new_score, moved = simulate_move(board, move, current_score)
        if moved:
            evaluated_score = evaluate_board(simulated_board)
            if evaluated_score > best_score:
                best_score = evaluated_score
                best_move = move

    if best_move is None:
        print("No valid moves available.")
        return None, None
    
    return best_move, best_score
