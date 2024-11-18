from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Represent a Node object as a string"""
        """Magic method - If a node is called (ex- lines 21 and 22),"""
        """the code returns the return value of the __str__ function"""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
print(one)
print(courses)


# to_str code no longer needed as it functions the same as the __str__ magic method
def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str"""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a linked list"""
    # 1. If head is followed by None?
    #    Return head's value
    # 2. Else, return the last of the rest of the list (next Node)
    if head.next is None:
        return head.value  # Base case!
    else:
        return last(head.next)  # Recursive Case


print(last(one))  # Expect 2
print(last(courses))  # Expect 301


def recursive_range(start: int, end: int) -> Node | None:
    """Build a linked list recursively from start up until end (not inclusive)"""
    if start > end:
        raise ValueError("Invalid use of recursive_range")
    if start == end:
        return None
    else:
        # Recursive case:
        # Intuition: handle the first case based on the specific call
        # Build the rest of the list using the builder function recursively
        rest: Node | None = recursive_range(start + 1, end)
        return Node(start, rest)


a: Node | None = recursive_range(2, 8)
b: Node | None = recursive_range(110, 112)
print(a)
print(b)


def factorial(n: int) -> int:
    """Compute the factorial of n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))
