def process_and_reverse_list(list1: list[int]) -> list[int]:
    square_list = []
    process_list = []
    reverse_list = []
    for x in list1:
        square_list.append(x**2)
    idx = 0
    while idx < len(square_list):
        if idx < len(square_list) - 1:
            process_list.append(square_list[idx] + square_list[idx + 1])
        else:
            process_list.append(square_list[idx])
        idx += 2
    idx2 = len(process_list) - 1
    while idx2 >= 0:
        reverse_list.append(process_list[idx2])
        idx2 -= 1
    return reverse_list


print(process_and_reverse_list([7, 8, 9]))
