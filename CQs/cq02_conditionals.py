"""Challenge Question 02 - Conditions, Local Variables, and User Input"""

__author__ = "730488976"


def guess_a_number() -> None:  # Defines the function with no input and returns None
    secret: int = 7  # Defined variable "secret" as an int of 7
    x: str = input(
        "Guess a number:"
    )  # Defined variable "x" as a str input in response to "Guess a number:"
    print("Your guess was " + x)  # Prints "Your guess was" + the user input
    if int(x) == secret:  # x is converted to an int
        print("You got it!")  # Prints in the event the user input is 7
    elif int(x) < secret:  # x is converted to an int
        print("Your guess was too low! The secret number is " + str(secret))
        """Prints in the event the user input is less than 7"""
        """converts variable "secret" to a str to allow concatanation"""
    else:
        print("Your guess was too high! The secret number is " + str(secret))
        """Prints in the event the user input is greater than 7"""
        """converts variable "secret" to a str to allow concatanation"""


if __name__ == "__main__":
    guess_a_number()  # allows code to run
