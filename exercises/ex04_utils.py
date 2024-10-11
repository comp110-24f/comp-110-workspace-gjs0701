"""EX04 - list Utility Functions"""

__author__ = "730488976"


def all(
    input: list[int], num: int
) -> bool:  # defines function with a list parameter and int parameter; returns bool
    if len(input) == 0:  # if input list is empty
        return False  # return False if list is empty
    for x in input:  # analyzes every value in list input
        if x != num:  # enters if the value in the list doesn't equal num parameter
            return False  # return false if value in list doesn't equal num parameter
    return True  # return True if all values in list are the same as num


def max(
    input: list[int],
) -> int:  # defines function with a list paramter; returns an int
    if len(input) == 0:  # if input list is empty
        raise ValueError("max() arg is an empty List")  # error message if list is empty
    largest = input[0]  # local variable set the equal the first value in input
    for x in input:  # analyzes all values in input
        if x > largest:  # if a value in the list is bigger than largest
            largest = x  # replace largest with x
    return largest  # return largest value in list


def is_equal(
    List1: list[int], List2: list[int]
) -> bool:  # defines function with two list parameters; returns bool
    if len(List1) != len(List2):  # If the two lists are not equal in length
        return False  # return false if two lists are not equal in length
    idx: int = 0  # establish idx for while loop
    while idx < len(List1):  # enter while loop if idx is less than length of List1
        if (
            List1[idx] != List2[idx]
        ):  # If the values of the two lists at the same index are not equal
            return False  # return False if values at the same index are not equal
        idx += 1  # increase idx so every value is checked
    return True  # return True if all values in the two lists are the same


def extend(
    a: list[int], b: list[int]
) -> None:  # defines function with two list parameters; returns None
    for x in b:  # analyzes all values in list b
        a.append(x)  # add all values in list b to list a
