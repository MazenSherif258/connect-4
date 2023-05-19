import numpy as np
from board import Board
import time
import random

# GAME LINK
# http://kevinshannon.com/connect4/


def main():
    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        print("\n########################################\n")

        # print(np.array(game_board))
        # break
        column, score = minimax(np.array(game_board), 5, -np.Inf, np.Inf, True)

        print("col: ", column)
        # exit()

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        random_column = random.randint(0, 6)
        board.select_column(column)

        time.sleep(2)


# Constants
EMPTY = 0
AI_AGENT = 1
COMPUTER = 2
ROWS = 6
COLS = 7


def evaluate_window(window, ai_agent):
    """
    Evaluate a window of four cells for a given ai_agent.
    Returns the score for the window.
    """
    score = 0
    opponent = AI_AGENT if ai_agent == COMPUTER else COMPUTER

    if window.count(ai_agent) == 4:
        score += 100
    elif window.count(ai_agent) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(ai_agent) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opponent) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def score_position(board, ai_agent):
    """
    Score the entire board for a given ai_agent.
    Returns the total score for the ai_agent's positions.
    """
    score = 0

    # Check horizontal
    for r in range(ROWS):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLS - 3):
            window = row_array[c:c+4]
            score += evaluate_window(window, ai_agent)

    # Check vertical
    for c in range(COLS):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROWS - 3):
            window = col_array[r:r+4]
            score += evaluate_window(window, ai_agent)

    # Check diagonal (positive slope)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, ai_agent)

    # Check diagonal (negative slope)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window, ai_agent)

    return score


def is_terminal_node(board):
    return (np.count_nonzero(board == EMPTY) == 0) or (score_position(board, AI_AGENT) == 100) or (score_position(board, COMPUTER) == 100)


def minimax(board, depth, alpha, beta, maximizing_ai_agent):

    valid_moves = get_valid_moves(board)
    is_terminal = is_terminal_node(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if score_position(board, COMPUTER) == 100:
                return None, 100000000000000
            elif score_position(board, AI_AGENT) == 100:
                return None, -10000000000000
            else:  # Game is over, no more valid moves
                return None, 0
        else:  # Depth is zero
            return None, score_position(board, COMPUTER)

    if maximizing_ai_agent:
        value = -np.Inf
        print("valid_moves: ", valid_moves)
        column = np.random.choice(valid_moves)
        for col in valid_moves:
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            make_move(temp_board, row, col, COMPUTER)
            new_score = minimax(temp_board, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:  # Minimizing ai_agent
        value = np.Inf
        print("valid_moves: ", valid_moves)
        column = np.random.choice(valid_moves)
        for col in valid_moves:
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            make_move(temp_board, row, col, AI_AGENT)
            new_score = minimax(temp_board, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

# Helper functions


def get_valid_moves(board):
    valid_moves = []
    for col in range(COLS):
        if is_valid_move(board, col):
            valid_moves.append(col)
    return valid_moves


def is_valid_move(board, col):
    return board[0][col] == EMPTY


def get_next_open_row(board, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            return row


def make_move(board, row, col, ai_agent):
    board[row][col] = ai_agent


if __name__ == "__main__":
    main()
