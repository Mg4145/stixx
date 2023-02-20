""" Player Class """


class Player:

    def __init__(self, name: str) -> None:
        """ Initialize the player's name and score """
        self.name = name
        self.score = 0
        self.left = 0
        self.right = 0

    def __str__(self) -> str:
        """ Return the player's name and score """
        return f"{self.name}: {self.score}"

    def update_hands(self, left: int, right: int) -> None:
        """ Update the player's hands """
        pass

