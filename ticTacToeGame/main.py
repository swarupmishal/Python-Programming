from lib.board import Board
from lib.player import Player
import time

if __name__ == '__main__':
    board = Board()
    print("***************************************************")
    print("  Welcome to Tic-Tac-Toe")
    print("***************************************************")
    board.print_board()

    human = Player()
    computer = Player(is_human=False)
    game_over = False

    while not game_over:
        game_over = human.conduct_player_action(board)
        if not game_over:
            game_over = computer.conduct_player_action(board)
        else:
            break
    print("Game Over!")
