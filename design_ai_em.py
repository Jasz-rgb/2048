import sys
import pygame
from pygame.time import Clock
from math import log2
from move import *
from generate import generate_initial_tiles, generate_new_tile
from expectimax import find_best_move
from checkwin import is_game_over, has_won
import multiprocessing as mp

#this code uses the expectiminimax algorithm to play the game 2048

size = width, height = 480, 500
playRegion = 480, 480
FPS = 40

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
fontColor = (85, 52, 42)
defaultTileColor = (238, 228, 218)
tileBorderColor = fontColor

# Game
boardSize = 4
score = 0  # Defining score variable globally
ai = False  # Initializing ai variable

def drawBoard(screen, board, score, moves):
    """
    Draws the game board and tiles on the screen.
    """
    screen.fill(black)  # Fill the screen with white color
    for i in range(boardSize):
        for j in range(boardSize):
            color = defaultTileColor  # Default tile color
            numberText = ""  # Default text for the tile
            if board[i][j] != 0:
                gComponent = 235 - log2(board[i][j]) * ((235 - 52)/(boardSize**2))
                color = (235, gComponent, 52)
                numberText = str(board[i][j])  # Convert tile value to string
            rect = pygame.Rect(j * playRegion[0]/boardSize,
                               i*playRegion[1]/boardSize,
                               playRegion[0]/boardSize,
                               playRegion[1]/boardSize,)  # Tile position and size
            pygame.draw.rect(screen, color, rect)  # Drawing the tile
            pygame.draw.rect(screen, fontColor, rect, 1)  # Drawing the tile border
            fontImage = tileFont.render(numberText, 0, fontColor)  # Rendering the tile number
            if fontImage.get_width() > playRegion[0]/boardSize:
                fontImage = pygame.transform.scale(fontImage, (playRegion[0]/boardSize, fontImage.get_width()*playRegion[0]/fontImage.get_width()))
            screen.blit(fontImage, (j * playRegion[0]/boardSize + (playRegion[0]/boardSize - fontImage.get_width())/2,
                        i * playRegion[1]/boardSize + (playRegion[1]/boardSize - fontImage.get_height())/2))
    fontImage = scoreFont.render("Score: " + str(score), 1, white)  # Rendering the score
    screen.blit(fontImage, (1, playRegion[1]+1))  # Drawing the score on the screen
    fontImage = scoreFont.render("Moves: " + str(moves), 1, white)  # Rendering the moves
    screen.blit(fontImage, (100, playRegion[1]+1))  # Drawing the moves on the screen
    pygame.display.flip()  # Update the display

def handleInput(event, board, score, moves):
    """ w,a,s,d for up, left, down, right respectively """
    """ r to restart """
    """ ESC to exit """
    """ SPACE to toggle AI """
    global ai
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            print("Move up")
            board, score, moved = move_up(board, score)
            if moved:
                board = generate_new_tile(board)
                moves += 1
        elif event.key == pygame.K_a:
            print("Move left")
            board, score, moved = move_left(board, score)
            if moved:
                board = generate_new_tile(board)
                moves += 1
        elif event.key == pygame.K_s:
            print("Move down")
            board, score, moved = move_down(board, score)
            if moved:
                board = generate_new_tile(board)
                moves += 1
        elif event.key == pygame.K_d:
            print("Move right")
            board, score, moved = move_right(board, score)
            if moved:
                board = generate_new_tile(board)
                moves += 1
        elif event.key == pygame.K_r:
            board = [[0]*boardSize for _ in range(boardSize)]
            board = generate_initial_tiles(board)
            score = 0  # Resets score on restart
            moves = 0  # Resets moves on restart
            invalid_moves = set()
        elif event.key == pygame.K_ESCAPE:
            pool.close()
            pool.terminate()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            ai = not ai
    return board, score, moves


def gameLoop():
    global clock, screen, tileFont, scoreFont, pool
    mp.freeze_support()
    mp.set_start_method('spawn', force=True)  
    pool = mp.Pool(processes = 4)  # Initializes multiprocessing pool
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2048 Game")
    tileFont = pygame.font.SysFont("", 72)
    scoreFont = pygame.font.SysFont("", 24)
    clock = pygame.time.Clock()  # Initializes clock here
    board = [[0]*boardSize for _ in range(boardSize)]
    board = generate_initial_tiles(board)
    score = 0
    moves = 0
    invalid_moves = set()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pool.close()
                pool.terminate()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board = [[0]*boardSize for _ in range(boardSize)]
                    board = generate_initial_tiles(board)
                    score = 0 
                    moves = 0 
                    invalid_moves = set()
                elif event.key == pygame.K_ESCAPE:
                    pool.close()
                    pool.terminate()
                    sys.exit()

        # Uses Expectimax to make moves automatically
        if not is_game_over(board):
            nextBestMove = find_best_move(board)
            if has_won(board):
                print("🎉 You reached 2048! Game Over.")
                drawBoard(screen, board, score, moves)
                pygame.time.wait(3000)  # wait 3 seconds to show final board
                pool.close()
                pool.terminate()
                pygame.quit()
                sys.exit()
            new_board, score, moved = simulate_move(board, nextBestMove, score)
            if moved:
                board = generate_new_tile(new_board)
                moves += 1
                invalid_moves.clear()
            else:
                print("Invalid move")
                invalid_moves.add(nextBestMove)
                continue

        drawBoard(screen, board, score, moves)
        pygame.display.flip()
        clock.tick(FPS)



if __name__ == "__main__":
    gameLoop()
    pygame.quit()
