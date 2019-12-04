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

    def checkstart(self, name):
        try:
            assert len(name) > 1 and len(name) < 15
        except AssertionError as a:
            return False