import random


class Die:

    def __init__(self):
        self._roll_value = None

    def roll_dice(self):
        self._roll_value = random.randint(1, 6)
        return self._roll_value

    @property
    def roll_value(self):
        return self._roll_value


class Player:

    def __init__(self, is_human, die):
        self._is_human = is_human
        self._die = die
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_human(self):
        return self._is_human

    @property
    def counter(self):
        return self._counter

    def roll(self):
        return self._die.roll_dice()

    def get_counter(self):
        return self._counter

    def roll_won(self):
        self._counter -= 1

    def roll_lost(self):
        self._counter += 1


class DiceGame:

    def __init__(self, human_player, computer_player):
        self._human_player = human_player
        self._computer_player = computer_player

    def start_game(self):
        print('\n=====================================================================')
        print('🎲 Welcome to the Dice Game!!')
        print('🎲 Let the game begin!! 🎲')
        print('=====================================================================')
        game_over = False
        while not game_over:
            game_over = self.start_round()

        winner = self.get_winner()
        self.end_game(winner)

    def start_round(self):
        # Welcome the User
        self.print_round_welcome()

        # Roll the dice
        self._human_player.roll()
        self._computer_player.roll()
        human_die_result = self._human_player.die.roll_value
        computer_die_result = self._computer_player.die.roll_value

        # Show the roll results
        self.show_dice(human_die_result, computer_die_result)

        if human_die_result > computer_die_result:
            self.update_counters(winner=human, looser=computer)
            print('You won this round!')
        elif human_die_result < computer_die_result:
            self.update_counters(winner=computer, looser=human)
            print('Computer won this round!')
        else:
            print('It was a tie!')

        # Show Counters
        self.show_counters_after_round()

        return self.is_game_over()

    def is_game_over(self):
        if self._human_player.get_counter() == 0 or self._human_player.get_counter() == 20:
            return True
        else:
            return False

    def get_winner(self):
        if self._computer_player.get_counter() == 0:
            return self._computer_player
        else:
            return self._human_player

    def print_round_welcome(self):
        print('\n--------------------------New Round-----------------------------')
        key = input("Press any key to start the round and roll your dice 🎲. Enter 'exit' to end the game!")
        if key.lower() == 'exit':
            self.exit_game()

    @staticmethod
    def show_dice(human_die_result, computer_die_result):
        print(f'You rolled {human_die_result}!')
        print(f'Computer rolled {computer_die_result}!')

    @staticmethod
    def update_counters(winner, looser):
        winner.roll_won()
        looser.roll_lost()

    def show_counters_after_round(self):
        print(f'Scores after the current round, You:{self._human_player.get_counter()} '
              f'v/s Computer:{self._computer_player.get_counter()}!')

    @staticmethod
    def end_game(winner):
        if winner.is_human: # == self._computer_player:
            print('\n=========================================================')
            print('G A M E     O V E R ')
            print('Congratulations. You beat the computer!😃')
            print('=========================================================')
        else:
            print('\n=========================================================')
            print('G A M E     O V E R ')
            print('Computer won the game. Sorry...☹️')
            print('=========================================================')

    @staticmethod
    def exit_game():
        quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    human_die = Die()
    computer_die = Die()
    human = Player(True, human_die)
    computer = Player(False, computer_die)
    game = DiceGame(human, computer)
    game.start_game()