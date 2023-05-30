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