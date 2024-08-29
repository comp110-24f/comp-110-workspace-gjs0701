"""To determine the amount of supplies needed for a tea party with my friends"""

__author__ = "730488976"


def main_planner(guests: int) -> None:
    """Will calculate all code using just the number of guests attending"""
    """And previously integer values are transformed into string values"""
    """Calls the below functions with guests as the argument"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Defining how many tea bags we need for each person to have two"""
    return 2 * people


def treats(people: int) -> int:
    """Defining how many treats if they want 1.5 treats per tea"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Defining the cost of both tea bags and treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    """Makes the program runnable"""
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
