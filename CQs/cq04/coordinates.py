"""CQ04 - Coordinates - Importing and Scope Challenge Question"""

__author__ = "730488976"


def get_coords(
    xs: str, ys: str
) -> None:  # defines function get_coords with two string parameters. Returns None
    index1: int = 0  # declares local variable index1
    while index1 < len(xs):  # while loop if index1 is less than the length of xs
        index2 = 0  # declares local variable index2
        while index2 < len(ys):  # while loop if index2 is less than the length of ys
            print(
                f"({xs[index1]},{ys[index2]})"
            )  # prints a string of xs at index1 and ys at index2
            index2 += (
                1  # index2 increases by one so the next charatcer in ys can be printed
            )
        index1 += (
            1  # index1 increases by one so the next character in xs can be evaluated
        )
