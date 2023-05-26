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

    while True:
        human_move = human.get_human_move(board)
        board.submit_move(human, human_move)
        game_over = human.check_if_player_won(board)
        if game_over:
            board.print_board()
            print("You won!")
            break
        time.sleep(0.5)
        computer_move = computer.get_computer_move(board)
        board.submit_move(computer, computer_move)
        computer.check_if_player_won(board)
        if game_over:
            print("Computer won!")
            break

        board.print_board()
    print("Game Over!")
