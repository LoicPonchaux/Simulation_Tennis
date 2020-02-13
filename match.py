import Player.player as player
import Score.score as score
import random


class Match:
    def __init__(self):
        self.J1 = player.Player("Federer", "Roger", 37, 85, 85, 98, 89)
        self.J2 = player.Player("Nadal", "Rafa", 34, 98, 75, 78, 95)
        self.score = score.Score()

    def displayMatch(self):
        return self.J1.player_presentation() + " VS " + self.J2.player_presentation()

    def resultMatch(self):
        if (self.score.gameJ1.number > self.score.gameJ2.number):
            return "Vainqueur : " + self.J1.player_presentation()
        else:
            return "Vainqueur : " + self.J2.player_presentation()

    def play(self):
        while (self.score.gameJ1.number != 6 and self.score.gameJ2.number != 6):
            J1 = random.randint(0, 100)
            J2 = random.randint(0, 100)
            if (J1 > J2):
                self.score.gameJ1.countGame()
            else:
                self.score.gameJ2.countGame()
        return self.resultMatch() + " " + self.score.displayScore()


M1 = Match()

print(M1.displayMatch())
print(M1.play())
