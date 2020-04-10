import Score.game as game
import Score.set as set
import Player.player as player

class Score():
    """
    Un score est constitué de :
    -   Le premier set
    -   Le deuxième set
    -   Le troisième set
    -   Le joueur 1
    -   Le joueurs 2
    """

    def __init__(self, J1, J2):
        self.set1 = set.Set(1)
        self.set2 = set.Set(2)
        self.set3 = set.Set(3)
        self.J1 = J1
        self.J2 = J2

    def displayScore(self):

        """Fonction permettant l'affichage du score
        Au tennis, on affiche toujours le score du vainqueur en premier
        Et le score du dernier set ne se dit pas si il n'a pas eu lieu
        Par exemple on dit 6/3 6/3 que 3/6 3/6 0/0"""

        if (self.set1.winner == self.set2.winner):
            if (self.J1 == self.set1.winner):
                return "Vainqueur : " + str(self.J1.player_presentation()) + \
                       "\n2 set à 0\n" + \
                       str(self.set1.gameJ1.number) + "/" + str(self.set1.gameJ2.number) + "\n" + \
                       str(self.set2.gameJ1.number) + "/" + str(self.set2.gameJ2.number)
            else:
                return "Vainqueur : " + str(self.J2.player_presentation()) + \
                       "\n2 set à 0\n" + \
                       str(self.set1.gameJ2.number) + "/" + str(self.set1.gameJ1.number) + "\n" + \
                       str(self.set2.gameJ2.number) + "/" + str(self.set2.gameJ1.number)
        else:
            if (self.J1 == self.set3.winner):
                return "Vainqueur : " + str(self.J1.player_presentation()) + \
                       "\n2 set à 1\n" + \
                       str(self.set1.gameJ1.number) + "/" + str(self.set1.gameJ2.number) + "\n" + \
                       str(self.set2.gameJ1.number) + "/" + str(self.set2.gameJ2.number) + "\n" + \
                       str(self.set3.gameJ1.number) + "/" + str(self.set3.gameJ2.number)
            else:
                return "Vainqueur : " + str(self.J2.player_presentation()) + \
                       "\n2 set à 1\n" + \
                       str(self.set1.gameJ2.number) + "/" + str(self.set1.gameJ1.number) + "\n" + \
                       str(self.set2.gameJ2.number) + "/" + str(self.set2.gameJ1.number) + "\n" + \
                       str(self.set3.gameJ2.number) + "/" + str(self.set3.gameJ1.number)

    def incrementScore(self, val):
        """On incrémente le nombre de jeux en fonction du vainqueur du jeu"""
        if (val == 1):
            self.gameJ1.countGame()
        if (val == 2):
            self.gameJ2.countGame()
