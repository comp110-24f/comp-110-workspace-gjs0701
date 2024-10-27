"""EX06 - Dictionary Utility Functions"""

__author__ = "730488976"


def invert(x: dict[str, str]) -> dict[str, str]:
    dupes = []
    inverted = {}
    for key in x:
        value = x[key]
        if value in dupes:
            raise KeyError("Inverted dictionary leads to duplicate keys")
        dupes.append(value)
        inverted[value] = key
    return inverted


def favorite_color(x: dict[str, str]) -> str:
    color_count: dict[str, int] = {}
    first_occurrence = {}
    for key in x:
        color = x[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
            first_occurrence[color] = key

    most_popular_color = ""
    max_count = 0

    for color in color_count:
        if color_count[color] > max_count:
            most_popular_color = color
            max_count = color_count[color]

    return most_popular_color


def count(x: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for elem in x:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    return result


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for elem in x:
        first_letter = elem[0].lower()
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(elem)
    return result


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    if day not in attendance_log:
        attendance_log[day] = []
    if student not in attendance_log[day]:
        attendance_log[day].append(student)
