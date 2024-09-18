"""To determine the amount of supplies needed for a tea party with my friends"""

__author__ = "730488976"


def main_planner(guests: int) -> None:
    """Will calculate all code using just the number of guests attending"""
    """And previously integer values are transformed into string values"""
    """Calls the below functions with guests as the argument"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # convert guest to str and concatenate
    print(
        "Tea Bags: " + str(tea_bags(guests))
    )  # concatenate str result of tea_bags with variable guests
    print(
        "Treats: " + str(treats(guests))
    )  # concatenate str result of treats with variable guests
    print(
        "Cost: $" + str(cost(tea_bags(guests), treats(guests)))
    )  # concatenate str result of cost with variable guests


def tea_bags(people: int) -> int:  # int variable people; returns an int
    """Defining how many tea bags we need for each person to have two"""
    return 2 * people  # returns 2 * people


def treats(people: int) -> int:  # int variable people; returns an int
    """Defining how many treats if they want 1.5 treats per tea"""
    return int(tea_bags(people=people) * 1.5)  # returns rsult of tea_bags * 1.5


def cost(
    tea_count: int, treat_count: int
) -> float:  # int variables tea_count, treat_count; returns a float
    """Defining the cost of both tea bags and treats"""
    return (tea_count * 0.50) + (
        treat_count * 0.75
    )  # returns total cost based on tea_count and treat_count


if __name__ == "__main__":
    """Makes the program runnable"""
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # provides user with a prompt; input is used to define guests
