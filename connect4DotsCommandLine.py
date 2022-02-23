import numpy as np
import sys

ROW_COUNT = 6
COL_COUNT = 7
PLAYER_ONE_PIECE = 1
PLAYER_TWO_PIECE = 2

# track if game is finished
game_over = False

# create and return game board
def create_board():
    return np.zeros((ROW_COUNT,COL_COUNT
))

# game board
board = create_board()

# track players turn
turn = 0

# put piece to speficied place
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# check if location is valid to put piece
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if(board[row][col] == 0):
            return row
    return -1

# flip board to show in terminal
def print_board(board):
    print(np.flip(board,0))

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

print_board(board)

while not game_over:
    if turn == 0:
        col = int(input("Player One Make Your Selection (0-6):"))
        if(is_valid_location(board, col)):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER_ONE_PIECE)

            if winning_move(board, PLAYER_ONE_PIECE):
                print("PLAYER ONE WIN!!!")
                game_over = True
        turn = 1
    else:
        col = int(input("Player Two Make Your Selection (0-6):"))
        if(is_valid_location(board, col)):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER_TWO_PIECE)

            if winning_move(board, PLAYER_TWO_PIECE):
                print("PLAYER TWO WIN!!!")
                game_over = True
        turn = 0
    print_board(board)