"""Challenge Question 05 - Lists Practice"""

__author__ = "730488976"

list_1: list[int] = [1, 2, 3]  # define global variable list_1
list_2: list[int] = list_1  # define global variable list_2


def manual_append(
    a: list[int], b: int
) -> (
    None
):  # define function manual_append with one list parameter and one int parameter
    a.append(b)  # adds int b to the end of list a


def double(c: list[int]) -> None:  # define function double with one list parameter
    idx: int = 0  # set index equal to zero for while loop
    while idx < len(c):  # while loop for when index is less than the length of list c
        c[idx] = 2 * c[idx]  # doubles the value for every number in the list
        idx += 1  # increase index so each number can be doubled


double(list_2)  # calls function double using list_2 as an argument
print(list_1)  # prints list_1
print(list_2)  # prints list_2
