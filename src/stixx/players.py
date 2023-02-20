""" Player Class """


class Player:
    def __init__(self, name: str) -> None:
        """Initialize the player's name and score"""
        self.name = name
        self.left = 1
        self.right = 1

    # def __str__(self) -> str:
    #     """Return the player's name"""
    #     return self.name + " " + self.current_hand()

    def is_both_empty(self) -> bool:
        """Check if either player has no sticks left"""
        return self.left == 0 or self.right == 0

    def current_hand(self) -> str:
        """Return the current hand"""
        return f"L: {self.left}\nR: {self.right}"
