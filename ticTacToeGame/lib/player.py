import random
from lib.move import Move
import numpy as np


class Player:

    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, is_human=True):
        self._is_human = is_human
        if is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    @staticmethod
    def get_human_move(board):
        while True:
            user_input = int(input("Please enter your move (1-9): "))
            move = Move(user_input)
            if move.is_valid() and board.check_if_cell_empty(move):
                break
            else:
                print("Please enter an integer between 1 and 9.")
        return move

    def get_computer_move(self, board):
        available_positions = self.get_available_positions(board)
        random_choice = random.choice(available_positions)
        move = Move(random_choice)
        print("Computer move (1-9): ", move.value)
        return move

    @staticmethod
    def get_available_positions(board):
        available_positions = []
        for row in board.game_board:
            for col in row:
                if col in range(1, 10):
                    available_positions.append(col)
        return available_positions

    def check_if_player_won(self, board):
        player_won = False
        board_arr = np.array(board.game_board)
        transposed_board_arr = board_arr.transpose().tolist()
        diagonal_elements = board_arr.diagonal().tolist()
        anti_diagonal_elements = board_arr[::-1].diagonal().tolist()

        # Checking win by each row
        if not player_won:
            for row in board.game_board:
                player_won = self.check_list_full_with_player_markers(row)
                if player_won:
                    break

        # Checking win by each column
        if not player_won:
            for og_col_as_row in transposed_board_arr:
                player_won = self.check_list_full_with_player_markers(og_col_as_row)
                if player_won:
                    break

        # Checking win by diagonal
        if not player_won:
            player_won = self.check_list_full_with_player_markers(diagonal_elements)

        # Checking win by anti diagonal
        if not player_won:
            player_won = self.check_list_full_with_player_markers(anti_diagonal_elements)

        return player_won

    def check_list_full_with_player_markers(self, elements):
        player_count = 0
        for element in elements:
            if element == self._marker:
                player_count += 1
            else:
                return False
        if player_count == 3:
            return True
