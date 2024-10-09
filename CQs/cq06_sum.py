"""Challenge Question 06 - Summing the elements of a list using different loops"""

__author__ = "730488976"


def w_sum(
    vals: list[float],
) -> float:  # function w_sum with a list of floats as a parameter; returns None
    total = 0  # local variable total
    idx = 0  # local variable idx
    while idx < len(vals):  # while loop to index all values in the list vals
        total += vals[idx]  # sums all values in the list vals
        idx += 1  # allows while loop to check all values
    return total  # returns sum of all values in list


def f_sum(
    vals: list[float],
) -> float:  # function f_sum with a list of floats as a parameter; returns None
    total = 0  # local variable total
    for x in vals:  # checks all values in list
        total += x  # sums all values in list
    return total  # returns sum of all values in list


def f_range_sum(
    vals: list[float],
) -> float:  # function f_range_sum with a list of floats as a parameter; returns None
    total = 0.0  # local variable total
    for x in range(
        len(vals)
    ):  # checks all values in list between index 0 and len(vals)
        total += vals[x]  # sums all values in range in list
    return total  # returns sum of all values in range in list
