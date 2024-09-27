"""EX03 - Wordle - Recreation of the popular NYT game."""

__author__ = "730488976"

"""Global variables for the green, yellow, and white square emojis"""
WHITE_BOX: str = "\U00002B1C"  # white square emoji
GREEN_BOX: str = "\U0001F7E9"  # green square emoji
YELLOW_BOX: str = "\U0001F7E8"  # yellow square emoji


def input_guess(secret_word_len: int) -> str:
    """Checks whether the input guess is the same length as the secret word"""
    guess: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # Prompts user to input a guess
    while (
        len(guess) != secret_word_len
    ):  # While loop if guess length is not equal to secret word length
        guess = input(
            f"That wasn't {secret_word_len} chars! Try again:"
        )  # Prompt user to guess again
    return (
        guess  # guess is returned and stored if guess length equals secret word length
    )


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Function that checks secret_word at each index for the presence of char_guess"""
    assert (
        len(char_guess) == 1
    )  # ensures length of char_guess is 1. Returns error if not
    index: int = 0  # sets index for while loop
    while index < len(
        secret_word
    ):  # while loop if index is less than length of secret word
        if char_guess == secret_word[index]:
            return True  # Returns True if char_guess is found in secret_word at index
        else:
            index += (
                1  # Index increases if char_guess is not found in secret_word at index
            )
    return False  # Returns False if char_guess is never found in secret_word


def emojified(guess: str, secret: str) -> str:
    """Provides a visual of whether their guesses contain letters found in secret"""
    """Tells whether or not letter placement is correct"""
    assert len(guess) == len(secret)  # Ensures length of guess equals length of secret
    index: int = 0  # sets index for while loop
    hint: str = ""  # sets a blank string that emojis will add to to provide a hint
    while index < len(secret):  # while loop if index is less than length of secret
        if guess[index] == secret[index]:
            hint += (
                GREEN_BOX  # add a green box to hint if guess[index] == secret[index]
            )
        elif contains_char(
            secret, guess[index]
        ):  # calls contains_char to check if guess[index] is present in secret
            hint += YELLOW_BOX  # add a yellow box if guess[index] is present in secret
        else:
            hint += (
                WHITE_BOX  # add a white box if guess[index] is not present in secret
            )
        index += 1  # increase index so every character in guess can be checked
    return hint  # returns hint once all indexes are checked and we exit while loop


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # sets a turn number, starting at 1
    guess: str = ""  # sets variable guess
    hint: str = ""  # sets variable hint
    while turn <= 6:  # while loop if turn is less than or equal to 6
        print(f"=== Turn {turn}/6 ===")  # tells the player their turn
        guess = input_guess(
            len(secret)
        )  # calls input_guess, and sets guess equal to the user input
        hint = emojified(
            guess, secret
        )  # calls emojified and sets hint equal to the returned string
        print(hint)  # prints the hint for the player
        if guess == secret:
            print(
                f"You won in {turn}/6 turns!"
            )  # prints if the player guesses the secret
            turn = 7  # set turn to 7 so while loop is exited
        elif guess != secret and turn < 6:
            turn += 1  # increase the turn number if guess does not equal secret
        else:
            turn += 1  # will increase the turn so while loop is exited
            print(
                "X/6 - Sorry, try again tomorrow!"
            )  # prints messgae if player runs out of turns


if __name__ == "__main__":  # allows us to run program as a module
    main(secret="codes")  # allows other modules to import the functions and reuse them
