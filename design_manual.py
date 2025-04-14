import sys
import pygame
from pygame.time import Clock
from math import log2
from move import *
from generate import generate_initial_tiles, generate_new_tile

size = width, height = 480, 500
playRegion = 480, 480
FPS = 40

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
fontColor = (85, 52, 42)
defaultTileColor = (238, 228, 218)
tileBorderColor = fontColor
game_over_color = (255, 0, 0)  # Red
win_color = (0, 255, 0)        # Green
overlay_color = (0, 0, 0, 128)  # Semi-transparent black

# Game
boardSize = 4
score = 0 

def drawBoard(screen, board, score, moves, game_over=False, won=False):
    """
    Draws the game board and tiles on the screen.
    """
    screen.fill(black)
    
    for i in range(boardSize):
        for j in range(boardSize):
            color = defaultTileColor 
            numberText = "" 
            if board[i][j] != 0:
                gComponent = 235 - log2(board[i][j]) * ((235 - 52)/(boardSize**2))
                color = (235, gComponent, 52)
                numberText = str(board[i][j])
            rect = pygame.Rect(j * playRegion[0]/boardSize,
                               i*playRegion[1]/boardSize,
                               playRegion[0]/boardSize,
                               playRegion[1]/boardSize,) 
            pygame.draw.rect(screen, color, rect) 
            pygame.draw.rect(screen, fontColor, rect, 1) 
            fontImage = tileFont.render(numberText, 0, fontColor)  
            if fontImage.get_width() > playRegion[0]/boardSize:
                fontImage = pygame.transform.scale(fontImage, (playRegion[0]/boardSize, fontImage.get_width()*playRegion[0]/fontImage.get_width()))
            screen.blit(fontImage, (j * playRegion[0]/boardSize + (playRegion[0]/boardSize - fontImage.get_width())/2,
                        i * playRegion[1]/boardSize + (playRegion[1]/boardSize - fontImage.get_height())/2))
    
    fontImage = scoreFont.render(f"Score: {score}", True, white)
    screen.blit(fontImage, (10, playRegion[1] + 10))
    
    fontImage = scoreFont.render(f"Moves: {moves}", True, white)
    screen.blit(fontImage, (200, playRegion[1] + 10))

    if game_over or won:
        overlay = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay.fill(overlay_color)
        screen.blit(overlay, (0, 0))
        
        message = "You Win!" if won else "Game Over!"
        color = win_color if won else game_over_color
        font = pygame.font.SysFont("Arial", 64, bold=True)
        
        text = font.render(message, True, color)
        text_rect = text.get_rect(center=(width//2, height//2))
        screen.blit(text, text_rect)
        
        small_font = pygame.font.SysFont("Arial", 24)
        restart_text = small_font.render("Press R to restart", True, white)
        restart_rect = restart_text.get_rect(center=(width//2, height//2 + 50))
        screen.blit(restart_text, restart_rect)

    pygame.display.flip()

def handleInput(event, board, score, moves):
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
            score = 0  
            moves = 0  
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
    return board, score, moves

def gameLoop():
    global clock, screen, tileFont, scoreFont
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2048 Game")
    tileFont = pygame.font.SysFont("", 72)
    scoreFont = pygame.font.SysFont("", 24)
    clock = pygame.time.Clock() 
    board = [[0]*boardSize for _ in range(boardSize)]
    board = generate_initial_tiles(board)
    score = 0
    moves = 0

    while True:
        for event in pygame.event.get():
            board, score, moves = handleInput(event, board, score, moves)

        drawBoard(screen, board, score, moves)
        pygame.display.flip()
        clock.tick(FPS) 
if __name__ == "__main__":
    global screen, tileFont, scoreFont
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2048 Game")
    tileFont = pygame.font.SysFont("", 72)
    scoreFont = pygame.font.SysFont("", 24)
    gameLoop() 
    pygame.quit()
