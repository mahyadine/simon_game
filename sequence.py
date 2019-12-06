from random import *
import time
import os 


class Sequence():

    def __init__(self):
        self.numbers = []


    def add_random_number(self):
        number = randint(1,10)
        self.numbers.append(number)
