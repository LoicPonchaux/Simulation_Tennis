class Game():
    """
    Class pour gerer le nombre de jeux gagner
    :param number: compteur
    :type number: int
    """

    def __init__(self):
        self.number = 0

    def countGame(self):
        """
        Incremente de 1 le nombre de jeu gagner
        :return:
        """
        self.number += 1

    def compareGame(self, other):
        """
        Determine qui a le plus de jeu gagner
        En comparant le nombre de jeu par personne
        :param other: Joueur a comparer
        :return: Celui qui a le plus de jeux
        """
        if isinstance(other, self.__class__):
            return str(other.number) + " " + str(self.number)
