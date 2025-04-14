from print_board import print_board

# --- Game Logic Functions (These are used by both Manual and AI modes) ---
from move import *
from generate import create_board, generate_initial_tiles, generate_new_tile
from checkwin import is_game_over, has_won

# --- AI Model ---
from ai import evaluate_all_moves

# --- Expectimax function ---
from expectimax import get_best_expectimax_move

# --- Main Game Loop ---
def main():
    board = create_board()
    board = generate_initial_tiles(board)
    moves = 0
    score = 0

    game_mode = input("Play manually (m) or let AI play (a/e)? ").lower()

    if game_mode == 'm':
        while not is_game_over(board) and not has_won(board):
            print("Score: ", score)
            print("Moves: ", moves)
            print_board(board)
            move = input("Enter move (w/a/s/d): ").lower()

            if move == 'w':
                board, score, moved = move_up(board, score)
            elif move == 'a':
                board, score, moved = move_left(board, score)
            elif move == 's':
                board, score, moved = move_down(board, score)
            elif move == 'd':
                board, score, moved = move_right(board, score)
            else:
                print("Invalid input. Please enter w, a, s, or d.")
                continue

            if moved:
                board = generate_new_tile(board)
                moves += 1
            else:
                print("Invalid move")
                continue

    elif game_mode == 'a':
        print("AI mode is activated")
        invalid_moves = set()

        while not is_game_over(board) and not has_won(board):
            print("Score: ", score)
            print("Moves: ", moves)
            print_board(board)

            best_move, _ = evaluate_all_moves(board, invalid_moves, score)  # AI evaluation returns best move and eval score

            if best_move is None:
                print("The AI is unable to find any more moves.")
                break

            print(f"AI chose: {best_move}")

            if best_move == 'w':
                new_board, score, moved = move_up(board, score)
            elif best_move == 'a':
                new_board, score, moved = move_left(board, score)
            elif best_move == 's':
                new_board, score, moved = move_down(board, score)
            elif best_move == 'd':
                new_board, score, moved = move_right(board, score)
            else:
                print(f"Unexpected move: {best_move}")
                break

            if moved:
                board = generate_new_tile(new_board)
                moves += 1
                invalid_moves.clear()
            else:
                print(f"AI made an invalid move: {best_move}")
                invalid_moves.add(best_move)
                if len(invalid_moves) == 4:
                    print("No possible moves available.")
                    print("GAME OVER")
                    break

    elif game_mode == 'e':
        print("AI (Expectimax) mode is activated")
        invalid_moves = set()
        while not is_game_over(board) and not has_won(board):
            print("Score: ", score)
            print("Moves: ", moves)
            print_board(board)

            best_move = get_best_expectimax_move(board, invalid_moves=set(), depth=3)

            if best_move is None:
                print("The AI is unable to find any more moves.")
                break

            print(f"AI chose: {best_move}")

            if best_move == 'w':
                new_board, score, moved = move_up(board, score)
            elif best_move == 'a':
                new_board, score, moved = move_left(board, score)
            elif best_move == 's':
                new_board, score, moved = move_down(board, score)
            elif best_move == 'd':
                new_board, score, moved = move_right(board, score)
            else:
                print(f"Unexpected move: {best_move}")
                break

            if moved:
                board = generate_new_tile(new_board)
                moves += 1
                invalid_moves.clear()
            else:
                print(f"AI made an invalid move: {best_move}")
                invalid_moves.add(best_move)
                if len(invalid_moves) == 4:
                    print("No possible moves available.")
                    print("GAME OVER")
                    break


    else:
        print("Invalid game mode selected.")
        return

    print_board(board)
    if has_won(board):
        print("You win!")
    else:
        print("Game over!")
    print(f"Total moves: {moves}")
    print(f"Final score: {score}")

if __name__ == "__main__":
    main()
