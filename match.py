import Player.player as player
import Score.score as score
import random


class Match:
    def __init__(self, lastNameJ1, nameJ1, lastNameJ2, nameJ2):
        self.J1 = player.Player(lastNameJ1, nameJ1, 37, 85, 85, 50, 50)
        self.J2 = player.Player(lastNameJ2, nameJ2, 34, 98, 75, 50, 50)
        self.score = score.Score()
        self.nbJeu = 6
        self.nbSet = 2
        self.numberGame = 0

    def displayMatch(self):
        return self.J1.player_presentation() + " VS " + self.J2.player_presentation()

    def resultMatch(self):
        # if (self.score.gameJ1.number > self.score.gameJ2.number):
        #    return "Vainqueur : " + self.J1.player_presentation()
        # else:
        #    return "Vainqueur : " + self.J2.player_presentation()
        pass

    def play(self):
        match = True
        set = 1;
        while (match):
            if (set == 1):
                match = self.playSet(self.score.set1)
                if (match == False and set == 1):
                    print(set, match)
                    set = 2
                    match = True
            if (set == 2):
                match = self.playSet(self.score.set2)

        # return self.resultMatch() + " " + self.score.displayScore()
        return self.score.displayScore()

    def playSet(self, set):
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
                set.defineWinner(self.J1.lastname)
            else:
                set.defineWinner(self.J2.lastname)
            return False
        return True

J1lastname = input("Nom Joueur 1\n")
J1name = input("Prénom Joueur 1\n")

J2lastname = input("Nom Joueur 2\n")
J2name = input("Prénom Joueur 2\n")

M1 = Match(J1lastname, J1name, J2lastname, J2name)
print(M1.displayMatch())
print(M1.play())
print(M1.score.set1.winner)
input()
