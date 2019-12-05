from random import *
import time
import os 


class Sequence():

    def __init__(self):
        self.numbers = [12, 5, 56, 34]


    def add_random_number(self):
        number = randint (1,10)
        self.numbers.append(number)
