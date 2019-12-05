class Player ():
    
    def __init__(self):
        self.name = None
        self.score = 0
        
    def start(self):
        name = input("Veuillez entrer votre nom pour jouer :")
        while self.checkstart(name) is False:
            print("Merci de rentrer un nom valide ")
            name = input("Veuillez entrer votre nom pour jouer :")
        self.name = name
        print (" Bonjour {} je vous souhaite bonne chance".format(name))
        print (" Le jeu va commencer ")

    def checkstart(self, name):
        if len(name) > 1 and len(name) < 15:
            return True
        else:
            return False