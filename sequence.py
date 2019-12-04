from random import *

class Sequence():

    def __init__(self):
        self.computer = None

    def number(self):
        computer = randint (1,50)
        self.computer = computer
        print (computer)
