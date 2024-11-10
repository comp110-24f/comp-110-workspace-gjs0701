"""File to define Bear class."""

__author__ = "730488976"


class Bear:
    """Creates class Bear with values age and hunger_score."""

    age: int
    hunger_score: int

    def __init__(self):
        """Function to initialize the Bear class."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """Function designed to increase age by 1 and decrease hunger by 1 each day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Function to increased hunger_score based on number of fish eaten."""
        self.hunger_score += num_fish
