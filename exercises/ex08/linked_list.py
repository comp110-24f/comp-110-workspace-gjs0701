"""More Practice with Linked Lists."""

from __future__ import annotations

__author__ = "730488976"


class Node:
    """Creating Node Class to use in later functions."""

    value: int  # class parameter
    next: Node | None  # class parameter

    def __init__(self, value: int, next: Node | None):
        """Initializes Node."""
        self.value = value  # initializing value
        self.next = next  # initializing next

    def __str__(self) -> str:
        """Represent a Node object as a string."""
        """Magic method."""
        rest: str = "?"
        if self.next is None:
            rest = "None"  # prints at the end of the node when their is no next value
        else:
            rest = str(self.next)  # if there's a next node, we call str on it
        return f"{self.value} -> {rest}"  # prints all the node values in a list


def value_at(head: Node | None, index: int) -> int:
    """Prints the node value at a certain index."""
    if head is None:  # If there isn't a node
        raise IndexError("Index is out of bounds on the list")
    if index == 0:
        return head.value  # return value of first node if index is 0
    else:
        return value_at(
            head.next, index - 1
        )  # keep calling value_at until index reaches 0,
    # indicates we've reached the value for our index


def max(head: Node | None) -> int:
    """Return max value of multiple nodes."""
    if head is None:  # no node exists
        raise ValueError("Cannot call max with None.")
    if head.next is None:  # if we reach the end of our nodes
        return head.value
    next_max = max(head.next)  # find the max value in the rest of the list
    if head.value > next_max:  # checks if current value is more than next max
        return head.value
    else:
        return next_max


def linkify(items: list[int]) -> Node | None:
    """Turn a list of integers into a series of nodes."""
    if not items:  # if items is empty
        return None
    else:
        rest: Node = Node(
            items[0], linkify(items[1:])
        )  # recursive function that creates nodes from the list
    return rest  # returns the nodes


def scale(head: Node | None, factor: int) -> Node | None:
    """Takes a series of nodes and multiplies the values by a factor."""
    if not head:  # if no nodes
        return None
    else:  # if nodes exist
        scaled: Node = Node(
            factor * head.value, scale(head.next, factor)
        )  # multiply the value by the factor and then call scale again with next node
    return scaled  # return scaled nodes
