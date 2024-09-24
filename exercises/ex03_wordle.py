"""EX03 - Wordle - Recreation of the popular NYT game."""

__author__ = "730488976"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(secret_word_len: int) -> str:
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while True:
        if len(guess) == secret_word_len:
            return guess
        else:
            guess: str = input(f"That wasn't {secret_word_len} chars! Try again:")


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Function that checks secret_word at each index for the presence of char_guess"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if char_guess == secret_word[index]:
            return True
        else:
            index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Provides a visual of whether their guesses contain letters found in secret"""
    """Tells whether or not letter placement is correct"""
    assert len(guess) == len(secret)
    count: int = 0
    hint: str = ""
    while count < len(secret):
        if guess[count] == secret[count]:
            hint += GREEN_BOX
        elif contains_char(secret, guess[count]):
            hint += YELLOW_BOX
        else:
            hint += WHITE_BOX
        count += 1
    return hint


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    guess: str = ""
    hint: str = ""
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        hint = emojified(guess, secret)
        print(hint)
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            turn = 7
        elif guess != secret and turn < 6:
            turn += 1
        else:
            turn += 1
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
