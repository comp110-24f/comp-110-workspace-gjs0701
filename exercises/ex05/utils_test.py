"""EX05 - List Unit Tests"""

__author__ = "730488976"


from exercises.ex05.utils import only_evens, sub, add_at_index  # imports functions
import pytest  # imports pytest


def test_only_evens_returns_correct_value() -> (
    None
):  # test function that makes sure only_evens returns the correct value
    input: list[int] = [2, 3, 6, 8, 9]  # defines an input list to test
    assert only_evens(input) == [
        2,
        6,
        8,
    ]  # assert that only_evens should return a list with only the even numbers


def test_only_evens_does_not_mutate_list() -> (
    None
):  # test function that makes sure only_evens does not mutate list
    input: list[int] = [2, 3, 6, 8, 9]  # defines an input list to test
    only_evens(input)  # calls function using input
    assert input == [
        2,
        3,
        6,
        8,
        9,
    ]  # assert that the original list (input) is not mutated


def test_only_evens_edge_case_no_evens() -> (
    None
):  # test function that makes sure only_evens works with a list of odds
    input: list[int] = [
        1,
        3,
        5,
        7,
        9,
    ]  # defines an input list of odd numbers to test (edge case)
    assert only_evens(input) == []  # assert that the resulting list is empty


def test_sub_returns_correct_value() -> (
    None
):  # test function that makes sure sub returns correct values
    input: list[int] = [5, 10, 15, 20, 25]  # defines an input list of integers
    x: int = 1  # defines a start index
    y: int = 4  # defines an end index
    assert sub(input, x, y) == [
        10,
        15,
        20,
    ]  # assert that sub returns a subset of input containing values between x and y-1


def test_sub_does_not_mutate_list() -> (
    None
):  # test function that makes sure sub does not mutate list
    input: list[int] = [5, 10, 15, 20, 25]  # defines an input list of integers
    x: int = 1  # defines a start index
    y: int = 4  # defines an end index
    sub(input, x, y)  # calls sub using input, x, y
    assert input == [5, 10, 15, 20, 25]  # assert that input does not mutate


def test_sub_negative_start_index() -> (
    None
):  # test function that sub works with negative start index
    input: list[int] = [5, 10, 15, 20, 25]  # defines an input list of integers
    x: int = -2  # defines a negative starting input (edge case)
    y: int = 4  # defines an end index
    assert sub(input, x, y) == [
        5,
        10,
        15,
        20,
    ]  # assert that sub still returns expected values


def test_add_at_index_returns_None() -> (
    None
):  # test function that add_at_index returns None
    input: list[int] = [5, 7, 8, 9, 10]  # defines an input list of integers
    x: int = 6  # defines an element to add to input
    y: int = 1  # defines the index element will be added to
    assert add_at_index(input, x, y) is None  # assert that add_at_index returns None


def test_add_at_index_does_mutate_list() -> (
    None
):  # test function that add_at_index does mutate list
    input: list[int] = [5, 7, 8, 9, 10]  # defines an input list of integers
    x: int = 6  # defines an element to add to input
    y: int = 1  # defines the index element will be added to
    add_at_index(input, x, y)  # calls add_at_index using input, x, y
    assert input == [
        5,
        6,
        7,
        8,
        9,
        10,
    ]  # assert that element is added at index of input, and list is mutated


def test_add_at_index_raises_indexerror() -> (
    None
):  # test function that add_at_index raises index error
    input: list[int] = [5, 7, 8, 9, 10]  # define an input list of integers
    x: int = 6  # defines an element to add to input
    y: int = -3  # defines a negative index where the element will be added (edge case)
    with pytest.raises(IndexError):  # using pytest, check if IndexError is raised
        add_at_index(
            input, x, y
        )  # calls add_at_index with input, x, y to see if it raises IndexError
