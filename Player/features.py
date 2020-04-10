class Features:
    """
    Une fiche technique est constitué de
    -   Un coup droit
    -   Un revers
    -   Un service
    -   Un retour
    Chiffres entre 1 et 100
    """

    def __init__(self, forehand, backhand, service, back):
        """
        Constructeur
        :param forehand: int
        :param backhand: int
        :param service: int
        :param back: int
        """
        self.forehand = forehand
        self.backhand = backhand
        self.service = service
        self.back = back


