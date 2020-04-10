import Score.game as game


class Set():
    """Classe set est défini par :
    -   Numéro de set (1, 2 ou 3)
    -   Nombre de jeu Joueur1
    -   Nombre de jeu Joueur2
    -   Vainqueur du set"""

    def __init__(self, nb):
        self.number = nb
        self.gameJ1 = game.Game()
        self.gameJ2 = game.Game()
        self.winner = None


    def defineWinner(self, Player):
        """Fonction permetant de définir le vainqueur du set"""
        self.winner = Player
