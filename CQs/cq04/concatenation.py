"""CQ04 - Concatenation - Importing and Scope Challenge Question"""

__author__ = "730488976"

word1: str = "happy"  # global variable declaration
word2: str = "tuesday"  # global variable declaration


def concat(
    word1: str, word2: str
) -> str:  # defines function concat with global variables serving as parameters
    return word1 + word2  # returns the concatenation of variables word1 and word2


if (
    __name__ == "__main__"
):  # prevents the print function from being imported to another program
    print(concat)  # prints result of concat
