import random
from lib.move import Move


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
        # TODO: Logic to not use already selected move
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
