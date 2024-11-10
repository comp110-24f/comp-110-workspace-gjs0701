def short_words(list1: list[str]) -> list[str]:
    new_list = []
    for x in list1:
        if len(x) < 5:
            new_list.append(x)
        else:
            print(f"{x} is too long!")
    return new_list


weather: list[str] = ["sun", "cloud", "sky"]
print(short_words(weather))
