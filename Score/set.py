import Score.game as game


class Set():

    def __init__(self, nb):
        self.number = nb
        self.gameJ1 = game.Game()
        self.gameJ2 = game.Game()
        self.winner = None

    """Méthode pour incrémenter un set"""

    def defineWinner(self, Player):
        self.winner = Player
