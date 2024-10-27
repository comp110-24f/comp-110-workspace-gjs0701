"""Challenge Question 07 - More Practice with Unit Tests"""

__author__ = "730488976"


from CQs.cq07.find_max import (
    find_and_remove_max,
)  # imports our function so we can test it


def test_return_expected() -> (
    None
):  # tests if function returns the largest value in a list
    input: list[int] = [13, 10, 4, 13]  # creates a local variable, input, to test with
    assert (
        find_and_remove_max(input) == 13
    )  # checks to see if our function, with input, returns 13


def test_return_mutated_list() -> (
    None
):  # tests if largest value(s) is removed from a list
    input: list[int] = [13, 10, 4, 13]  # creates a local variable, input, to test with
    find_and_remove_max(input)  # calls the function
    assert input == [
        10,
        4,
    ]  # checks to see if the list is now missing the largest value(s)


def test_return_unconventional_input() -> (
    None
):  # tests whether function returns correct value for empty list
    input: list[int] = []  # creates a local variable, input, to test with
    assert find_and_remove_max(input) == -1  # checks to see if an empty list returns -1
