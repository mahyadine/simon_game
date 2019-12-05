import time
import os
from sequence import Sequence
from player import Player


class ControllerGame:

    def __init__(self):
        self.player = Player()
        self.sequence = Sequence()

    def player_initialise(self):
        self.player.start()

    def display_sequence(self):
        self.sequence.add_random_number()
        for element in self.sequence.numbers :
            print(element)
            time.sleep(2)
            os.system("clear")
    