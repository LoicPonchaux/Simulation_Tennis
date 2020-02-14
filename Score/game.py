class Game():

    def __init__(self):
        self.number = 0

    """Méthode pour incrémenter un jeu"""

    def countGame(self):
        self.number += 1

    """Méthode pour l'affichage des jeux  du set"""

    def compareGame(self, other):
        if isinstance(other, self.__class__):
            return str(other.number) + " " + str(self.number)
