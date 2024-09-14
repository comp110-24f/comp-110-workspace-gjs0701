"""Both code functions below return the same thing"""

"""Just written in a different way"""
"""However they would have different memory diagrams"""


def speak(sound: str, repeat: int) -> str:
    return sound * repeat


print(speak(sound="woof", repeat=3))
print(speak(sound="meow", repeat=2))


def speak(sound: str, repeat: int) -> None:
    print(sound * repeat)


speak(sound="woof", repeat=3)
speak(sound="meow", repeat=2)
