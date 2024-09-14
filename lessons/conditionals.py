def less_than_10(num: int) -> None:
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number")
    print("This is the the end of the function")


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    if alarm is True:
        return "Wake up! Go to Comp110!"
    else:
        return "Keep sleeping. You deserve it. :)"


print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
