from lib.board import Board
from lib.move import Move
from lib.player import Player

if __name__ == '__main__':
    board = Board()
    print("***************************************************")
    print("  Welcome to Tic-Tac-Toe")
    print("***************************************************")
    board.print_board()

    human = Player()
    computer = Player(is_human=False)

    human_move = human.get_human_move(board)
    board.submit_move(human, human_move)
    computer_move = computer.get_computer_move(board)
    board.submit_move(computer, computer_move)
