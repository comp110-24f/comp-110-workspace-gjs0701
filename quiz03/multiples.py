def multiples(list1: list[int]) -> list[bool]:
    new_list = []
    if list1[0] % list1[len(list1) - 1] == 0:
        new_list.append(True)
    for x in range(1, len(list1)):
        if list1[x] % list1[x - 1] == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list


print(multiples([2, 3, 4, 8, 16, 2, 4, 2]))
