from random import *
import time
import os 


class Sequence():

    def __init__(self):
        self.numbers = []
        self.sleep = None
        self.randint = None


    def add_random_number(self):
        number = randint(1,100)
        self.numbers.append(number)


    
