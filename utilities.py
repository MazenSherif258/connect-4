import numpy as np
from game import COLS, ROWS, EMPTY, AI_AGENT, COMPUTER


def get_valid_moves(board):
    valid_moves = []
    for col in range(COLS):
        if is_valid_move(board, col):
            valid_moves.append(col)
    return valid_moves


def is_valid_move(board, col):
    return board[0][col] == EMPTY


def is_terminal_node(board):
    return (np.count_nonzero(board) == COLS*ROWS) or (score_position(board, AI_AGENT) == 100) or (score_position(board, COMPUTER) == 100)


def score_position(board, player):

    score = 0

    # vertical
    for c in range(COLS):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROWS - 3):
            window = col_array[r:r+4]
            score += evaluate_window(window, player)

    # horizontal
    for r in range(ROWS):
        row_array = [int(i) for i in list(board[r])]
        for c in range(COLS - 3):
            window = row_array[c:c+4]
            score += evaluate_window(window, player)

    # positive slope
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, player)

    # negative slope
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            window = [board[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, player)

    return score


def evaluate_window(window, player):

    score = 0
    opponent = AI_AGENT if player == COMPUTER else COMPUTER

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opponent) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def get_next_open_row(board, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            return row


def move(board, row, col, player):
    board[row][col] = player
