""" Player Class """


class Player:
    def __init__(self, name: str) -> None:
        """Initialize the player's name and score"""
        self.name = name
        self.left = 1
        self.right = 1

    def is_both_empty(self) -> bool:
        """Check if either player has no sticks left"""
        return self.left == 0 and self.right == 0

    def current_hand(self) -> str:
        """Return the current hand"""
        return f"{self.left} {self.right}"

    def update(self, hand: str, value: int) -> None:
        """Update the player's hand"""
        if hand == "L":
            self.left = (self.left + value) % 5 if (self.left + value) % 5 != 0 else 0
        else:
            self.right = (self.right + value) % 5 if (self.right + value) % 5 != 0 else 0
