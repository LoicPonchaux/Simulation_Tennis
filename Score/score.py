import Score.game as game


class Score():

    def __init__(self):
        self.gameJ1 = game.Game()
        self.gameJ2 = game.Game()

    def displayScore(self):
        if (self.gameJ1.number > self.gameJ2.number):
            return str(self.gameJ1.number) + " Jeux à " + str(self.gameJ2.number)
        else:
            return str(self.gameJ2.number) + " Jeux à " + str(self.gameJ1.number)

    def incrementScore(self, val):
        if (val == 1):
            self.gameJ1.countGame()
        if (val == 2):
            self.gameJ2.countGame()
