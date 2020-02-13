import Score.game as game


class Score():

    def __init__(self):
        self.gameJ1 = game.Game()
        self.gameJ2 = game.Game()

    def displayScore(self):
        return str(self.gameJ1.number) + " Jeu à " + str(self.gameJ2.number)

    def incrementScore(self, val):
        if (val == 1):
            self.gameJ1.countGame()
        if (val == 2):
            self.gameJ2.countGame()
