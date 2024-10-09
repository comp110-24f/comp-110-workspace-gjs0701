"""Basic syntax of lists"""

"""Creating a blank list"""
my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal
# Literal and constrcter syntax do the same thing

my_numbers.append(1.5)  # adds 1.5 to the list my_numbers


"""Creating a populated list"""
game_points: list[int] = [102, 86, 94]
# print(game_points[2])  # prints the list game_points at index 2

game_points[1] = 72  # changes 86 to 72

len(game_points)  # tells us length of a list

game_points.pop(1)  # removes the item at index 1


def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


display(game_points)
