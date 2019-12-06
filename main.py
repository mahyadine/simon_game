from player import Player
from sequence import Sequence
from controllerGame import ControllerGame


if __name__ == '__main__':
    controllerGame = ControllerGame()
    controllerGame.player_initialise()

    while True:
        controllerGame.display_sequence()
        answer = controllerGame.user_play()
        if answer == False: 
            controllerGame.replay()

