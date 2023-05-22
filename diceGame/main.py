import random


class Die:

    def __init__(self):
        self._roll_value = None

    @staticmethod
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
        self._die.roll_dice()

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
        print('Welcome to the Dice Game!! You can press escape key to exit the game.')
        print('Let the game begin!!')
        game_over = False
        while not game_over:
            game_over = self.start_round()
        winner = self.get_winner()
        if winner == self._computer_player:
            print('Computer was able to beat you!')
        else:
            print('You beat the computer!')

    def start_round(self):
        key = input("Press any key to start the round and roll your dice. Enter 'exit' to end the game!")
        if key.lower() == 'exit':
            self.exit_game()
        self._human_player.die.roll_dice(human_die)
        human_die_result = self._human_player.die.roll_value
        print(f'You rolled {human_die_result}!')
        self._computer_player.die.roll_dice(computer_die)
        computer_die_result = self._computer_player.die.roll_value
        print(f'Computer rolled {computer_die_result}!')
        if human_die_result > computer_die_result:
            human.roll_won()
            computer.roll_lost()
            print('You won this round!')
        elif human_die_result < computer_die_result:
            human.roll_lost()
            computer.roll_won()
            print('Computer won this round!')
        else:
            print('It was a tie!')
        print(f'Scores after the current round, You:{human.get_counter()} v/s Computer:{computer.get_counter()}!')

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

    def exit_game(self):
        quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    human_die = Die()
    computer_die = Die()
    human = Player(True, human_die)
    computer = Player(False, computer_die)
    game = DiceGame(human, computer)
    game.start_game()

