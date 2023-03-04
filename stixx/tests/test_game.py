import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from game import Game
from players import Player


class TestGame(unittest.TestCase):
    def tearUp(self):
        player1 = Player("Bob")
        player2 = Player("Sue")
        self.game = Game(player1, player2)
        # self.game.play()

    def test_is_over_player1(self):
        self.tearUp()
        player1 = self.game.player1
        player2 = self.game.player2
        player2.left = 0
        player2.right = 0
        self.assertTrue(self.game.is_over())

    def test_is_over_player2(self):
        self.tearUp()
        player1 = self.game.player1
        player2 = self.game.player2
        player1.left = 0
        player1.right = 0
        self.assertTrue(self.game.is_over())

    def test__init__(self):
        self.tearUp()
        self.assertEqual(self.game.player1.name, "Bob")
        self.assertEqual(self.game.player2.name, "Sue")
        self.assertEqual(self.game.winner, None)

    def test_get_winner(self):
        self.tearUp()
        player1 = self.game.player1
        player2 = self.game.player2
        player2.left = 0
        player2.right = 0
        self.game.get_winner()
        self.assertEqual(self.game.winner, "Bob")

        self.tearDown()
        self.tearUp()
        player1 = self.game.player1
        player2 = self.game.player2
        player1.left = 0
        player1.right = 0
        self.game.get_winner()
        self.assertEqual(self.game.winner, "Sue")
