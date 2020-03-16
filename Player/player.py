import Player.identity as identity

import Player.features as features


class Player(identity.Identity, features.Features):

    def __init__(self, lastname, firstname, age, forehand, backhand, service, back):
        identity.Identity.__init__(self, lastname, firstname, age)
        features.Features.__init__(self, forehand, backhand, service, back)

    def player_presentation(self):
        return self.firstname + " " + self.lastname

