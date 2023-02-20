""" Game module """

import players
import random


class Game:
    def __init__(self, player1: players.Player, player2: players.Player) -> None:
        """Initialize a new game"""
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        # print(f"{player1 = }")
        # print(f"{player2 = }")
        # print(f"{player1.left = }")
        # print(f"{player1.right = }")
        # print(f"{player1.left = }")
        # print(f"{player1.right = }")
        # print(f"{player2.left = }")
        # print(f"{player2.right = }")

    def coin_toss(self) -> players.Player:
        """Randomly select who goes first"""
        return random.choice([self.player1, self.player2])

    def play(self) -> None:
        """Play the game"""

        # Select who goes first
        current_player = self.coin_toss()

        # Play the game
        while True:
            print(f"{current_player.name} goes first!")
            print(f"{current_player.name} is your turn!")

            print(f"{current_player.current_hand() = }")

            # if not self.is_both_empty(current_player):
            if  not current_player.is_both_empty():
                self.winner = (
                    self.player1.name if current_player == self.player2 else self.player2.name
                )
                break
        #     # Get the current player's move
        #     move = current_player.get_move()

        #     # Update the game state
        #     self.update(move)

        #     # Check if the game is over
        #     if self.is_over():
        #         break

        #     # Switch players
        #     current_player = self.player1 if current_player == self.player2 else self.player2

        # Display the final state of the game
        # print(self)

        # Display the winner
        print(f"{self.winner} wins!")
