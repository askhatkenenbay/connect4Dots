import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COL_COUNT = 7

PLAYER_ONE_PIECE = 1
PLAYER_TWO_PIECE = 2

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE/2 - 5)

# track if game is finished
game_over = False

# game board
board = np.zeros((ROW_COUNT,COL_COUNT))

# track players turn
turn = 0


# put piece to speficied place
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# check if location is valid to put piece
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if(board[r][col] == 0):
            return r
    return -1

# check if last move is winning move
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # Check postitive slop
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negative slop
    for c in range(COL_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

# draw game in pygame
def draw_board(board):
    for c in range(COL_COUNT):
	    for r in range(ROW_COUNT):
		    pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
		    pygame.draw.circle(screen, BLACK, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)


    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):		
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
    pygame.display.update()


pygame.init()

width = COL_COUNT * SQUARE_SIZE
height = (ROW_COUNT+1) * SQUARE_SIZE
size = (width, height)
screen = pygame.display.set_mode(size)

draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 77)

while not game_over:
    for event in pygame.event.get():
        # close game
        if event.type == pygame.QUIT:
            sys.exit()
        # move circle at top
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARE_SIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARE_SIZE/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE/2)), RADIUS)
        pygame.display.update()
        # process mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARE_SIZE))
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARE_SIZE))
                if(is_valid_location(board, col)):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER_ONE_PIECE)

                    if winning_move(board, PLAYER_ONE_PIECE):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

                turn = 1
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARE_SIZE))
                if(is_valid_location(board, col)):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER_TWO_PIECE)

                    if winning_move(board, PLAYER_TWO_PIECE):
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True
                turn = 0
            draw_board(board)
            if game_over:
                pygame.time.wait(3000)