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

    def test_valid_input(self):
        self.tearUp()
        self.assertTrue(self.game.valid_input("L"))
        self.assertTrue(self.game.valid_input("R"))
        self.assertFalse(self.game.valid_input("A"))
        self.assertFalse(self.game.valid_input("B"))

    def test_coin_toss(self):
        self.tearUp()
        self.game.coin_toss()
        self.assertTrue(self.game.current_player.name == "Bob" or self.game.current_player.name == "Sue")

    def test_switch_players(self):
        self.tearUp()
        current_player = self.game.current_player
        other_player = self.game.opponent

        self.game.switch_players()
        self.assertEqual(self.game.current_player, other_player)
        self.assertEqual(self.game.opponent, current_player)


    # def test_prompt_dialog(self):
    #     self.tearUp()
    #     # Assert that two strings are equal
    #     start = "-" * 80 + f"\n{self.game.current_player.name} goes first!"
    #     assert_equal = self.game.prompt_dialog("start")
    #     print(f"START: {start}")
    #     print(f"ASSERT_EQUAL: {assert_equal}")
    #     self.assertEqual(start, assert_equal)
    # self.game.prompt_dialog("turn")
    # self.game.prompt_dialog("over")
