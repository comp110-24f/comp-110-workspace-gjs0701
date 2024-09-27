"""CQ04 - Visualize - Importing and Scope Challenge Question"""

__author__ = "730488976"

from concatenation import concat  # imports function concat from module concatenation
from coordinates import (
    get_coords,
)  # imports function get_coords from module coordinates

x: str = "123"  # global variable declaration
y: str = "abc"  # global variable declaration

print(concat(x, y))  # prints concat with x and y serving as arguments
get_coords(x, y)  # calls get_coords with x andy serving as arguments
