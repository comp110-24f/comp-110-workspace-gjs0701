"""Challenge Question 07 - Finding the Maxiumum Value in a List"""

__author__ = "730488976"


def find_and_remove_max(
    input: list[int],
) -> int:  # defines function with a list of int as parameter, and returns int
    if len(input) == 0:  # checks if list is empty
        return -1  # if list is empty, return -1
    largest = input[
        0
    ]  # creates local variable largest, set equal to first index of input
    for x in input:  # checks all values in input
        if x > largest:  # if a value is larger than largest
            largest = x  # set largest equal to said value
    idx: int = 0  # creates local variable idx
    while idx < len(input):  # allows us to check every value in input
        if input[idx] == largest:  # if input at an index equals largest
            input.pop(idx)  # delete that value from input
        else:  # if input at an index does not equal largest
            idx += 1  # increase idx by 1 to check next value
    return largest  # return largest value
