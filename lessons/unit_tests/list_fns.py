def get_first(list1: list[str]) -> str:
    if len(list1) == 0:
        return ""
    return list1[0]


def remove_first(list1: list[str]) -> None:
    list1.pop(0)


def get_and_remove_first(list1: list[str]) -> str:
    first_elem: str = list1[0]
    list1.pop(0)
    return first_elem
