""" Main module for the application. """

import players
import game


def main() -> None:
    """ Main function """

    player_1 = players.Player("John")
    player_2 = players.Player("Jane")

    print(player_1)
    print(player_2)


if __name__ == "__main__":
    main()
