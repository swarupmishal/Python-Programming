from lib.die import Die
from lib.player import Player
from lib.dice_game import DiceGame

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    human_die = Die()
    computer_die = Die()
    human = Player(True, human_die)
    computer = Player(False, computer_die)
    game = DiceGame(human, computer)
    game.start_game()