class Board:

    # EMPTY_CELL = 0

    def __init__(self):
        # self.game_board = [[0, 0, 0],
        #                    [0, 0, 0],
        #                    [0, 0, 0],]
        self.game_board = [[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9],]

    def print_board(self):
        print("\nPositions:")
        self.print_board_with_positions()

        print("Board:")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column in range(1, 10):
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()
        print()

    @staticmethod
    def print_board_with_positions():
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    def submit_move(self, player, move):
        row, col = self.get_cell_position(move)
        if self.check_if_cell_empty(move):
            self.game_board[row][col] = player.marker

    def check_if_cell_empty(self, move):
        row, col = self.get_cell_position(move)
        value = self.game_board[row][col]
        if value in range(1, 10):
            return True
        else:
            print("Cell is already is use, you can mark another cell.")
            return False

    @staticmethod
    def get_cell_position(move):
        row = move.get_row()
        col = move.get_column()
        return row, col
