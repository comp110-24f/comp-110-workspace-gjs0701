def merge_lists(list1: list[str], list2: list[int]) -> dict[str, int]:
    new_dict = {}
    if len(list1) != len(list2):
        return new_dict
    for x in range(0, len(list1)):
        new_dict[list1[x]] = list2[x]
    return new_dict


print(merge_lists(["blue", "yellow", "red"], [5, 2, 4]))
