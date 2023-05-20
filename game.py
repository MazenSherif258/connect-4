import math

import numpy as np
from board import Board
import time
from GUI import GUI, MINIMAX

# GAME LINK
# http://kevinshannon.com/connect4/

# Constants
EMPTY = 0
AI_AGENT = 1
COMPUTER = 2
ROWS = 6
COLS = 7


def main():
    board = Board()
    gui = GUI()

    algorithm = gui.choice
    difficulty = gui.level

    time.sleep(3)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        print("\n########################################\n")

        if (algorithm == MINIMAX):
            column = minimax(np.array(game_board), difficulty, True)[0]
        else:
            column = alpha_beta_pruning(np.array(game_board),difficulty,-math.inf,math.inf,True)[0]

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column

        board.select_column(column)

        time.sleep(2)


def minimax(board, depth, maximizing_player):

    valid_moves = get_valid_moves(board)
    is_terminal = is_terminal_node(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if score_position(board, AI_AGENT) == 100:
                return None, 100000000000000
            elif score_position(board, COMPUTER) == 100:
                return None, -10000000000000
            else:
                return None, 0
        else:
            return None, score_position(board, AI_AGENT)

    if maximizing_player:
        score = -np.Inf
        print("valid_moves: ", valid_moves)
        column = np.random.choice(valid_moves)
        for col in valid_moves:
            row = get_next_open_row(board, col)
            copy_board = board.copy()
            move(copy_board, row, col, AI_AGENT)
            new_score = minimax(copy_board, depth - 1, False)[1]
            if new_score > score:
                score = new_score
                column = col
        return column, score
    else:
        score = np.Inf
        print("valid_moves: ", valid_moves)
        column = np.random.choice(valid_moves)
        for col in valid_moves:
            row = get_next_open_row(board, col)
            copy_board = board.copy()
            move(copy_board, row, col, COMPUTER)
            new_score = minimax(copy_board, depth - 1, True)[1]
            if new_score < score:
                score = new_score
                column = col
        return column, score

def alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):

    valid_moves = get_valid_moves(board)
    is_terminal = is_terminal_node(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if score_position(board, AI_AGENT) == 100:
                return None, 100000000000000
            elif score_position(board, COMPUTER) == 100:
                return None, -10000000000000
            else:
                return None, 0
        else:
            return None, score_position(board, AI_AGENT)

    if maximizing_player:
        score = -np.Inf
        # print("valid_moves: ", valid_moves)
        column = np.random.choice(valid_moves)
        for col in valid_moves:
            row = get_next_open_row(board, col)
            copy_board = board.copy()
            move(copy_board, row, col, AI_AGENT)
            new_score = alpha_beta_pruning(copy_board, depth - 1, alpha, beta, False)[1]
            if new_score > score:
                score = new_score
                column = col
            alpha = max(alpha, score)
            if alpha >= beta:
                break
        return column, score
    else:
        score = np.Inf
        # print("valid_moves: ", valid_moves)
        column = np.random.choice(valid_moves)
        for col in valid_moves:
            row = get_next_open_row(board, col)
            copy_board = board.copy()
            move(copy_board, row, col, COMPUTER)
            new_score = alpha_beta_pruning(copy_board, depth - 1, alpha, beta, True)[1]
            if new_score < score:
                score = new_score
                column = col
            beta = min(beta, score)
            if alpha >= beta:
                break
        return column,score



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


if __name__ == "__main__":
    main()


