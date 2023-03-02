""" Game module """

import players
import random

# TODO: Create is_valid method for Player class to check if the move is valid
# TODO: Add an extra move for the players


class Game:
    """Game class"""

    def __init__(
            self,
            player1: players.Player,
            player2: players.Player
    ) -> None:
        """Initialize a new game"""
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def coin_toss(self) -> players.Player:
        """Randomly select who goes first"""
        return random.choice([self.player1, self.player2])

    def is_over(self) -> bool:
        """Check if the game is over"""
        return self.player1.is_both_empty() or self.player2.is_both_empty()

    def game_over(self) -> None:
        """Game over function"""
        self.get_winner()
        print("*" * 80)
        print("Game over!\nFinal Hands: ")
        print(f"{self.player1.name}: {self.player1.current_hand()}")
        print(f"{self.player2.name}: {self.player2.current_hand()}\n")
        print(f"{self.winner} wins!")
        print("*" * 80)

    def get_winner(self) -> None:
        """Get the winner of the game"""
        if self.player1.is_both_empty():
            self.winner = self.player2.name
        elif self.player2.is_both_empty():
            self.winner = self.player1.name

    def play(self) -> None:
        """Play the game"""

        # Select who goes first
        current_player = self.coin_toss()
        opponent = (self.player1
                    if current_player == self.player2
                    else self.player2)
        print("-" * 80)
        print(f"{current_player.name} goes first!")

        # Play the game
        while True:
            print(f"{current_player.name} it's your turn!")
            print(f"Your current hand is: {current_player.current_hand()}")
            print(f"{opponent.name}'s hand is: {opponent.current_hand()}\n")

            # Get the current player's move

            value = (
                current_player.left
                if input("Which of your hands? (L/R): ").upper() == "L"
                else current_player.right
            )

            hand = input("Which opponent's hand? (L/R): ").upper()

            # Update the game state
            opponent.update(hand, value)

            # Check if the game is over
            if self.is_over():
                self.game_over()
                break

            # Switch players
            current_player, opponent = opponent, current_player
            print("-" * 80)
