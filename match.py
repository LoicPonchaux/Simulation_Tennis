import Player.player as player
import Score.score as score
import random


class Match:
    def __init__(self, lastNameJ1, nameJ1, lastNameJ2, nameJ2):
        self.J1 = player.Player(lastNameJ1, nameJ1, 37, 85, 85, 50, 50)
        self.J2 = player.Player(lastNameJ2, nameJ2, 34, 98, 75, 50, 50)
        self.score = score.Score()

    def displayMatch(self):
        return self.J1.player_presentation() + " VS " + self.J2.player_presentation()

    def resultMatch(self):
        if (self.score.gameJ1.number > self.score.gameJ2.number):
            return "Vainqueur : " + self.J1.player_presentation()
        else:
            return "Vainqueur : " + self.J2.player_presentation()

    def play(self):
        match = True
        nbJeu = 6
        numberGame = 0
        while (match):

            if numberGame % 2 == 0:
                J1 = random.randint(0, 10) * self.J1.service
                J2 = random.randint(0, 10) * self.J2.back
            else:
                J1 = random.randint(0, 10) * self.J1.back
                J2 = random.randint(0, 10) * self.J2.service
            if (J1 > J2):
                self.score.gameJ1.countGame()
            else:
                self.score.gameJ2.countGame()
            numberGame += 1
            if (self.score.gameJ1.number == 5 and self.score.gameJ2.number == 5):
                nbJeu += 1
            if (self.score.gameJ1.number == nbJeu or self.score.gameJ2.number == nbJeu):
                match = False
        return self.resultMatch() + " " + self.score.displayScore()


J1lastname = input("Nom Joueur 1\n")
J1name = input("Prénom Joueur 1\n")

J2lastname = input("Nom Joueur 1\n")
J2name = input("Prénom Joueur 1\n")

M1 = Match(J1lastname, J1name, J2lastname, J2name)
print(M1.displayMatch())
print(M1.play())
