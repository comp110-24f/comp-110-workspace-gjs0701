"""File to define Fish class."""

__author__ = "730488976"


class Fish:
    """Creates class Fish with value age."""

    age: int

    def __init__(self):
        """Function to initialize the Fish class."""
        self.age: int = 0
        return None

    def one_day(self):
        """Function designed to increase age by 1 and decrease hunger by 1 each day."""
        self.age += 1
        return None
