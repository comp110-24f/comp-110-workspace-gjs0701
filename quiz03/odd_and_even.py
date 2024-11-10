def odd_and_even(list1: list[int]) -> list[int]:
    new_list = []
    for x in range(0, len(list1)):
        if list1[x] % 2 != 0 and x % 2 == 0:
            new_list.append(list1[x])
    return new_list


print(odd_and_even([7, 8, 10, 10, 5, 12, 3, 2, 11, 8]))
