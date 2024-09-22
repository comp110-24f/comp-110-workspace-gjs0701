"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730488976"

"""Prompts user for a five letter word and a letter"""
"""Returns where, and how many times, in the word that letter is found"""


def input_word() -> (
    str
):  # defines function input_word with no parameters and returns a string
    guess: str = input(
        "Enter a 5-character word: "
    )  # prompts user to input 5 letter word. Stored as local variable guess
    if len(guess) == 5:
        return guess  # if guess is 5 letters long, return guess
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # if guess is not 5 letters long, print an error and exit program
        return guess


def input_letter() -> (
    str
):  # defines function input_letter with no parameters and returns a string
    character: str = input(
        "Enter a single character:"
    )  # prompts user to input a single character. Stored as local variable character
    if len(character) == 1:
        return character  # if character is a single character, return character
    else:
        print("Error: Character must be a single character.")
        exit()  # if character is not a single character, print an error, exit program
        return character


def contains_char(
    guess: str, character: str
) -> (
    None
):  # defines function contains_char; guess and character are parameters; returns none
    index: int = 0  # establishes local variable index as an integer
    count: int = 0  # establishes local variable count as an integer
    print(
        "Searching for " + character + " in " + guess
    )  # relays message to user telling them what the program is doing
    while index < len(
        guess
    ):  # loop that checks each index location of guess. Exits loop if index==len(guess)
        if (
            character == guess[index]
        ):  # enter if statement if character equals the guess at index
            print(
                character + " found at index " + str(index)
            )  # prints if character==guess[index]
            count += 1  # count increases by 1 if character==guess[index]
        index += 1  # index increases by one to check next index position on guess
    if count == 1:
        print(
            str(count) + " instance of " + character + " found in " + guess
        )  # prints message if count==1
    elif count > 1:
        print(
            str(count) + " instances of " + character + " found in " + guess
        )  # prints message if count>1
    else:
        print(
            "No instances of " + character + " found in " + guess
        )  # prints is count==0


def main() -> (
    None
):  # main function that allows all functions to be called at the same time
    contains_char(guess=input_word(), character=input_letter())


if __name__ == "__main__":  # allows us to run program as a module,
    main()  # also allows other modules to import the functions and reuse them
