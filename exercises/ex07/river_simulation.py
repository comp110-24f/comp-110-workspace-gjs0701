"""Simulating our created rivers."""

__author__ = "730488976"

from exercises.ex07.river import River

"""Creates a new instance of a river class with 10 fish and 2 bears."""
my_river: River = River(num_fish=10, num_bears=2)

"""Lets us view the details of the river."""
my_river.view_river()
