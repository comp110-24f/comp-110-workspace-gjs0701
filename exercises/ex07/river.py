"""File to define River class."""

__author__ = "730488976"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Creates class River with attributes day, fish, bears."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages and eliminates any fish older than 3 and bears older than 5."""
        # new lists to add all young fish and young bears
        young_fish: list = []
        young_bears: list = []
        for x in self.fish:
            if x.age <= 3:
                young_fish.append(x)
        for x in self.bears:
            if x.age <= 5:
                young_bears.append(x)
        # set our old lists equal to the new lists
        self.fish = young_fish
        self.bears = young_bears
        return None

    def bears_eating(self):
        """Simulates bears eating; each bear eats 3 before the next bear can eat."""
        for bear in self.bears:
            if len(self.fish) > 5:
                bear.eat(num_fish=3)
                self.remove_fish(amount=3)
        return None

    def check_hunger(self):
        """Checks the hunger score and eliminates any bears with hunger below 0."""
        # new list to track nonhungry bears
        surviving_bears: list[Bear] = []
        for x in self.bears:
            if x.hunger_score >= 0:
                surviving_bears.append(x)
        # set old list equal to new list
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """If at least two fish, each pair with produce 4 offspring."""
        if len(self.fish) > 1:
            new_fish = len(self.fish) // 2 * 4
            for _ in range(new_fish):
                self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """If at least two bears, each pair will produce 1 offspring."""
        if len(self.bears) > 1:
            new_bears = len(self.bears) // 2
            for _ in range(new_bears):
                self.bears.append(Bear())
        return None

    def view_river(self):
        """Lets us view the river stats."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day seven times to simlate a week."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes a set amount of fish from self.fish."""
        for _ in range(amount):
            self.fish.pop(0)
