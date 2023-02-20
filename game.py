""" Game module """

import players
import random


class Game:

    def __init__(self, player1: players.Player, player2: players.Player) -> None:
        """ Initialize a new game """
        self.player1 = player1
        self.player2 = player2

    def coin_toss(self) -> players.Player:
        """ Randomly select who goes first """
        return random.choice([self.player1, self.player2])
