import math

import numpy as np
from board import Board
import time
from GUI import GUI, MINIMAX
import utilities

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
        # board.print_grid(game_board)
        # print("\n########################################\n")

        if (algorithm == MINIMAX):
            column = minimax(np.array(game_board), difficulty, True)[0]
        else:
            column = alpha_beta_pruning(
                np.array(game_board), difficulty, -math.inf, math.inf, True)[0]

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column

        board.select_column(column)

        time.sleep(2)


def minimax(board, depth, maximizing_player):

    valid_moves = utilities.get_valid_moves(board)
    is_terminal = utilities.is_terminal_node(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if utilities.score_position(board, AI_AGENT) == 100:
                return None, 100000000000000
            elif utilities.score_position(board, COMPUTER) == 100:
                return None, -10000000000000
            else:
                return None, 0
        else:
            return None, utilities.score_position(board, AI_AGENT)

    if maximizing_player:
        score = -np.Inf
        # print("valid_moves: ", valid_moves)
        column = np.random.choice(valid_moves)
        for col in valid_moves:
            row = utilities.get_next_open_row(board, col)
            copy_board = board.copy()
            utilities.move(copy_board, row, col, AI_AGENT)
            new_score = minimax(copy_board, depth - 1, False)[1]
            if new_score > score:
                score = new_score
                column = col
        return column, score
    else:
        score = np.Inf
        # print("valid_moves: ", valid_moves)
        column = np.random.choice(valid_moves)
        for col in valid_moves:
            row = utilities.get_next_open_row(board, col)
            copy_board = board.copy()
            utilities.move(copy_board, row, col, COMPUTER)
            new_score = minimax(copy_board, depth - 1, True)[1]
            if new_score < score:
                score = new_score
                column = col
        return column, score


def alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):

    valid_moves = utilities.get_valid_moves(board)
    is_terminal = utilities.is_terminal_node(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if utilities.score_position(board, AI_AGENT) == 100:
                return None, 100000000000000
            elif utilities.score_position(board, COMPUTER) == 100:
                return None, -10000000000000
            else:
                return None, 0
        else:
            return None, utilities.score_position(board, AI_AGENT)

    if maximizing_player:
        score = -np.Inf
        # print("valid_moves: ", valid_moves)
        column = np.random.choice(valid_moves)
        for col in valid_moves:
            row = utilities.get_next_open_row(board, col)
            copy_board = board.copy()
            utilities.move(copy_board, row, col, AI_AGENT)
            new_score = alpha_beta_pruning(
                copy_board, depth - 1, alpha, beta, False)[1]
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
            row = utilities.get_next_open_row(board, col)
            copy_board = board.copy()
            utilities.move(copy_board, row, col, COMPUTER)
            new_score = alpha_beta_pruning(
                copy_board, depth - 1, alpha, beta, True)[1]
            if new_score < score:
                score = new_score
                column = col
            beta = min(beta, score)
            if alpha >= beta:
                break
        return column, score


if __name__ == "__main__":
    main()
