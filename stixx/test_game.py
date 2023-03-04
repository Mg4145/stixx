import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from players import Player
from game import Game


class TestGame(unittest.TestCase):
    def tearUp(self):
        player1 = Player("Bob")
        player2 = Player("Sue")
        self.game = Game(player1, player2)
        self.game.play()

    def test_game_over(self):
        self.tearUp()
        player1 = self.game.player1
        player2 = self.game.player2
        player2.left = 0
        player2.right = 0
        self.assertTrue(self.game.is_over())
