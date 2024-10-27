"""EX05 - List Unit Tests"""

__author__ = "730488976"


"""Function that returns all the even numbers in a list, without mutating the list"""


def only_evens(
    input: list[int],
) -> list[int]:  # defines function with list[int] parameter; returns list[int]
    evens: list[int] = []  # creates local variable evens, an empty list[int]
    for x in input:  # checks all values in input
        if x % 2 == 0:  # if a value is even
            evens.append(x)  # add the even value to the list evens
    return evens  # return evens, now containing the even values


"""Function that generates a list which is a subset of the input list, between a
specified start index and the end index-1"""


def sub(
    input: list[int], start_idx: int, end_idx: int
) -> list[int]:  # defines funcion with paramters list[int], int, int; returns list[int]
    new_list: list[int] = []  # creates local variable new_list, an empty list[int]
    if (
        len(input) == 0 or start_idx >= len(input) or end_idx <= 0
    ):  # defines instances where we want to return an empty list
        return new_list  # return an empty list
    if start_idx < 0:  # checks if start_idx is negative
        start_idx = 0  # if it is negative, set start_idx equal to zero
    if end_idx > len(input):  # checks if end_idx is greater than the length of input
        end_idx = len(input)  # if so, set end_idx equal to the length of input
    idx: int = start_idx  # creates local variable idx, an int equal to start_idx
    while (
        start_idx <= idx < end_idx
    ):  # while loop that checks if idx is between start_idx and end_idx
        new_list.append(input[idx])  # add input at index idx to new_list
        idx += 1  # increase idx by 1 so all values are checked
    return new_list  # return new_list with correct subset values


"""Function that places an element into a list at a given index"""
"""A space is added to the end of the list, values are moved over, and the element is
placed in the space at the given index"""


def add_at_index(
    input: list[int], element: int, index: int
) -> None:  # defines function with parameters list[int], int, int; returns None
    if index < 0 or index > len(
        input
    ):  # checks if index lies outside the range of input
        raise IndexError("Index is out of bounds for the input list")  # error message
    input.append(0)  # add space to the end of input, so values can later be shifted
    idx: int = (
        len(input) - 1
    )  # creates local variable idx, an int equal to the length of input minus 1
    while idx > index:  # while loops that checks all values of input greater than index
        input[idx] = input[
            idx - 1
        ]  # shifts value to the right, giving space to add a new element
        idx -= 1  # decrease idx by 1 so all values are checked
    input[index] = (
        element  # with all values shifted, element is placed at the given index
    )
