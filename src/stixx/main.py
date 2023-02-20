""" Main module for the application. """

# import argparse
from players import Player
from game import Game


def main() -> None:
    """Main function"""

    player_1 = Player("John")
    player_2 = Player("Jane")

    stixx_game = Game(player_1, player_2)
    stixx_game.play()


if __name__ == "__main__":
    main()
