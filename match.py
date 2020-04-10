import Player.player as player
import Score.score as score
import random


class Match:
    """
    On joue le match ici on a donc :
    -   Joueur 1
    -   Joueur 2
    -   Le score
    -   Nombre de Jeux pour gagner un set
    -   Nombre de Sets pour gagner le match
    -   Nombre de Jeux jouer
    -   Vainqueur du match
    """
    def __init__(self, lastNameJ1, nameJ1, lastNameJ2, nameJ2):
        """
        :param lastNameJ1: str
        :param nameJ1: str
        :param lastNameJ2: str
        :param nameJ2: str
        """

        self.J1 = player.Player(lastNameJ1, nameJ1, 37, 85, 85, 50, 50)
        self.J2 = player.Player(lastNameJ2, nameJ2, 34, 98, 75, 50, 50)
        self.score = score.Score(self.J1, self.J2)
        self.nbJeu = 6
        self.nbSet = 2
        self.numberGame = 0
        self.winner = None

    def displayMatch(self):
        """
        Présentation du match
        :return: L'affiche du jour
        """
        return self.J1.player_presentation() + " VS " + self.J2.player_presentation()



    def play(self):
        """
        On joue le match
        :return: str
            Le score du match
        """

        # Tant que le match n'a pas de vainqueur on joue
        match = False
        # Début du premier set
        set = 1
        while (match == False):
            if (set == 1):
                match = self.playGame(self.score.set1)
                if (match == True):
                    set = 2
                    self.nbJeu = 6
                    match = False
            if (set == 2):
                match = self.playGame(self.score.set2)
                if (self.score.set1.winner == self.score.set2.winner):
                    self.winner = self.score.set1.winner
                    return self.score.displayScore()
                if (match == True):
                    set = 3
                    self.nbJeu = 6
                    match = False
            if (set == 3):
                match = self.playGame(self.score.set3)
        self.winner = self.score.set3.winner
        return self.score.displayScore()

    def playGame(self, set):
        """
        Permet de jouer un jeu
        :param set: l'objet set
        :return: Fin du set ou non
        """
        J1, J2 = self.determineServe()
        if (J1 > J2):
            set.gameJ1.countGame()
        else:
            set.gameJ2.countGame()
        self.numberGame += 1
        return self.determineEndSet(set)

    def determineServe(self):
        """
        On détermine qui a le service
        :return: int, int
            Score du calcul de chaque joueur
        """

        if self.numberGame % 2 == 0:
            J1 = random.randint(0, 10) * self.J1.service
            J2 = random.randint(0, 10) * self.J2.back
        else:
            J1 = random.randint(0, 10) * self.J1.back
            J2 = random.randint(0, 10) * self.J2.service
        return J1, J2

    def determineEndSet(self, set):
        """
        Détermine si le set est fini ou non
        :return: bool
            Fin du set ou non
        """
        if (set.gameJ1.number == 5 and set.gameJ2.number == 5):
            self.nbJeu += 1
            return False
        if (set.gameJ1.number == self.nbJeu or set.gameJ2.number == self.nbJeu):
            if (set.gameJ1.number == self.nbJeu):
                set.defineWinner(self.J1)
            else:
                set.defineWinner(self.J2)
            return True
        return False

J1lastname = input("Nom Joueur 1\n")
J1name = input("Prénom Joueur 1\n")

J2lastname = input("Nom Joueur 2\n")
J2name = input("Prénom Joueur 2\n")

M1 = Match(J1lastname, J1name, J2lastname, J2name)
print(M1.displayMatch())
print(M1.play())
input()
