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
        self.difficulty()


    def display_sequence(self):
        self.sequence.add_random_number()
        for element in self.sequence.numbers :
            print(element)
            time.sleep(2)
            os.system("clear")


    def computer_play(self):
        self.sequence.add_random_number()


    def user_play(self):
        for element in self.sequence.numbers:
            chose_player = int(input("Veuillez entrer votre réponse "))
            if chose_player != element:
                return False 


    def replay(self):
        print("Vous avez perdu dommage! ")
        while True:
            replay = input("Souhaitez vous rejouez oui ou non : ").lower()
            if replay == "oui":
                self.sequence.numbers = []
                break
            elif replay == "non":
                exit()
            else:
                print("Choisissez entre oui ou non ")


    def difficulty(self):
        level = int(input("Veuillez choisir le niveau \n 1 pour facile \n 2 pour intermediaire \n 3 pour avancé \n votre choix : "))

        if level == 1:
            self.sequence.sleep = 3 
            self.sequence.randint = 10
        elif level == 2:
            self.sequence.sleep = 2
            self.sequence.sleep = 20
        elif level == 3:
            self.sequence.sleep = 3
            self.sequence.sleep = 30
        else:
            print("Selectinner le niveau entre 1 et 3 ")

