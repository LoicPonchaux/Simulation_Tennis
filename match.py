import Player.player as player
import Score.score as score
import random


class Match:
    def __init__(self, lastNameJ1, nameJ1, lastNameJ2, nameJ2):
        self.J1 = player.Player(lastNameJ1, nameJ1, 37, 85, 85, 50, 50)
        self.J2 = player.Player(lastNameJ2, nameJ2, 34, 98, 75, 50, 50)
        self.score = score.Score(self.J1, self.J2)
        self.nbJeu = 6
        self.nbSet = 2
        self.numberGame = 0
        self.winner = None

    def displayMatch(self):
        return self.J1.player_presentation() + " VS " + self.J2.player_presentation()



    def play(self):
        match = True
        set = 1;
        while (match):
            if (set == 1):
                match = self.playGame(self.score.set1)
                if (match == False):
                    set = 2
                    self.nbJeu = 6
                    match = True
            if (set == 2):
                match = self.playGame(self.score.set2)
                if (self.score.set1.winner == self.score.set2.winner):
                    self.winner = self.score.set1.winner
                    return self.score.displayScore()
                if (match == False):
                    set = 3
                    self.nbJeu = 6
                    match = True
            if (set == 3):
                match = self.playGame(self.score.set3)
        # return self.resultMatch() + " " + self.score.displayScore()
        self.winner = self.score.set3.winner
        print(self.resultMatch())
        return self.score.displayScore()

    def playGame(self, set):
        if self.numberGame % 2 == 0:
            J1 = random.randint(0, 10) * self.J1.service
            J2 = random.randint(0, 10) * self.J2.back
        else:
            J1 = random.randint(0, 10) * self.J1.back
            J2 = random.randint(0, 10) * self.J2.service
        if (J1 > J2):
            set.gameJ1.countGame()
            # self.score.gameJ1.countGame()
        else:
            set.gameJ2.countGame()
            # self.score.gameJ2.countGame()
        self.numberGame += 1
        if (set.gameJ1.number == 5 and set.gameJ2.number == 5):
            self.nbJeu += 1
        if (set.gameJ1.number == self.nbJeu or set.gameJ2.number == self.nbJeu):
            if (set.gameJ1.number == self.nbJeu):
                set.defineWinner(self.J1)
            else:
                set.defineWinner(self.J2)
            return False
        return True

J1lastname = input("Nom Joueur 1\n")
J1name = input("Prénom Joueur 1\n")

J2lastname = input("Nom Joueur 2\n")
J2name = input("Prénom Joueur 2\n")

M1 = Match(J1lastname, J1name, J2lastname, J2name)
print(M1.displayMatch())
print(M1.play())
input()
