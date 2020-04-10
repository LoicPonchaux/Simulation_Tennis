import Player.identity as identity

import Player.features as features


class Player(identity.Identity, features.Features):
    """
    Classe Player est constitué de :
    -   Une identité (Nom, Prénom et âge)
    -   Une fiche technique du joueur (Coup droit, revers, service, retour)
    """

    def __init__(self, lastname, firstname, age, forehand, backhand, service, back):
        """
        :param lastname: str
        :param firstname: str
        :param age: int
        :param forehand: int
        :param backhand: int
        :param service: int
        :param back: int
        """

        identity.Identity.__init__(self, lastname, firstname, age)
        features.Features.__init__(self, forehand, backhand, service, back)

    def player_presentation(self):
        """
        Permet de présenter le joueur
        :return: str
            chaine de caractère avec les informations
        """

        return self.firstname + " " + self.lastname
