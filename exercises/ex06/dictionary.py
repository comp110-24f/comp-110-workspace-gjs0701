"""EX06 - Dictionary Utility Functions"""

__author__ = "730488976"


def invert(
    x: dict[str, str]
) -> dict[
    str, str
]:  # function definition with parameter x, a dict[str, str]; returns dict[str, str]
    """Invert the keys and the values of a dictionary"""
    dupes = []  # local variable; empty list to track duplicate keys to avoid key error
    inverted = {}  # local variable; new dict to hold inverted keys and values
    for key in x:  # checks all keys in x
        value = x[key]  # local variable equal to the value of a key in x
        if value in dupes:  # if the value is already in out dupes list
            raise KeyError(
                "Inverted dictionary leads to duplicate keys"
            )  # error to prevent the creation of duplicate keys
        dupes.append(value)  # add the value to the dupes list
        inverted[value] = key  # the value becomes the key and the key becomes the value
    return inverted  # returns the inverted dict


def favorite_color(
    x: dict[str, str]
) -> str:  # function definition with parameter x, dict[str,str]; returns str
    """From a dictionary of people's favorite colors, return consensus favorite color"""
    color_count: dict[str, int] = (
        {}
    )  # local variable; empty dict to track color frequency
    for key in x:  # checks all keys in dict x
        color = x[key]  # local variable color, that equals the value of a key in x
        if color in color_count:  # if color is already in color_count
            color_count[color] += 1  # increase the value at key color by 1
        else:  # if color is not in color_count
            color_count[color] = 1  # add new key to color_count with value of 1

    most_popular_color = ""  # local variable; empty str for most_popular_color
    max_count = 0  # local variable; int of 0 to track the color with highest count

    for color in color_count:  # checks all keys(colors) in color_count
        if (
            color_count[color] > max_count
        ):  # if the value at key(color) is more than max_count
            most_popular_color = (
                color  # set most_popular_color equal to that key(color)
            )
            max_count = color_count[
                color
            ]  # set max_count equal to the value of that key(color)

    return most_popular_color  # returns a str of the most popular color


def count(
    x: list[str],
) -> dict[
    str, int
]:  # function definition with parameter x, list[str]; returns dict[str, int]
    """Counts how many times a specific str appears in a list of str"""
    result: dict[str, int] = (
        {}
    )  # local variable; empty dict that will track how many times a word appears
    for elem in x:  # checks all words in x
        if elem in result:  # if the word is already a key in result
            result[elem] += 1  # increase the value of that key by 1
        else:  # if the word is not a key in result
            result[elem] = 1  # add a new key of that word and set the value equal to 1
    return (
        result  # return the dict counting the number of appearances of difference words
    )


def alphabetizer(
    x: list[str],
) -> dict[
    str, list[str]
]:  # function definition with parameter x, list[str]; returns dict[str, list[str]]
    """Given a list of words,"""
    """returns a dict of letters with the words that begin with that letter"""
    result: dict[str, list[str]] = {}  # local varibale; empty dict[str, list[str]]
    for elem in x:  # checks all elem in list x
        first_letter = elem[
            0
        ].lower()  # local variable; equals the first letter of elem in lowercase
        if first_letter not in result:  # if first_letter is not already in result
            result[first_letter] = (
                []
            )  # add new key to result with an empty list as the value
        result[first_letter].append(
            elem
        )  # append elem to the list value at key first_letter in result
    return (
        result  # return the dict of letters with the words that begin with that letter
    )


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> (
    None
):  # function def with three parameters: dict[str, list[str]], str, str; returns None
    """Takes the previous attendance and adds new attendance values"""
    if day not in attendance_log:  # if day is not already a key in attendance_log
        attendance_log[day] = (
            []
        )  # add a new key of that day with an empty list as the value
    if (
        student not in attendance_log[day]
    ):  # if the student has not already been marked present for day
        attendance_log[day].append(
            student
        )  # add that student to the list associated with that day
