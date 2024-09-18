"""Challenge Question 03 - While Loops"""

__author__ = "730488976"

"""Function that upon giving it a phrase, can search for a character"""
"""Will give back how many times said character appears"""


def num_instances(
    phrase: str, search_char: str
) -> (
    int
):  # def num_instances with two variables, phrase and search_char, both str returns int
    count: int = 0  # count track number of times search_char appears in phrase
    index: int = 0  # index tracks our letter placement in phrase
    while index < len(
        phrase
    ):  # makes sure the while loop will terminate once we reach the end of the phrase
        if (
            phrase[index] == search_char
        ):  # occurs if our letter placement in phrase matches that of search_char
            count = count + 1  # increase count since we found search_char in phrase
            index = index + 1  # moves our index to the next character in phrase
        else:  # occurs if phrase[index] != seach_char
            index = index + 1  # index increases and we move to next letter in phrase
    return count  # to end our function, we return the count value
