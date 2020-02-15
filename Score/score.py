import Score.game as game
import Score.set as set

class Score():

    def __init__(self):
        # self.gameJ1 = game.Game()
        # self.gameJ2 = game.Game()
        self.set1 = set.Set(1)
        self.set2 = set.Set(2)
        self.set3 = set.Set(3)

    def displayScore(self):
        if (self.set1.winner == self.set2.winner):
            return "2 set à 0\n" + \
                   str(self.set1.gameJ1.number) + "/" + str(self.set1.gameJ2.number) + "\n" + \
                   str(self.set2.gameJ1.number) + "/" + str(self.set2.gameJ2.number)
        else:
            return "2 set à 1\n" + \
                   str(self.set1.gameJ1.number) + "/" + str(self.set1.gameJ2.number) + "\n" + \
                   str(self.set2.gameJ1.number) + "/" + str(self.set2.gameJ2.number) + "\n" + \
                   str(self.set3.gameJ1.number) + "/" + str(self.set3.gameJ2.number)
        # if (self.gameJ1.number > self.gameJ2.number):
        #    return str(self.gameJ1.number) + " Jeux à " + str(self.gameJ2.number)
        # else:
        #    return str(self.gameJ2.number) + " Jeux à " + str(self.gameJ1.number)
        pass

    def incrementScore(self, val):
        if (val == 1):
            self.gameJ1.countGame()
        if (val == 2):
            self.gameJ2.countGame()


score = Score()
score.set1.defineWinner("nadal")
print(score.displayScore())
val = score.set1.gameJ1
