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