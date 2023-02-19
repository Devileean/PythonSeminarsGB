def arithmetic_sequence(first_element: int, element_diff: int, quantity_elements:int):
    sequence = [first_element]
    for i in range(2, quantity_elements + 1):
        sequence.append(first_element + (i - 1) * element_diff)
    return sequence


def create_list(x: int):
    my_list = []
    for _ in range(x):
        my_list.append(int(input('Введите число: ')))
    return my_list


def indexes_of_numbers(num_lst: list, start: int, end: int):
    indexes_list = []
    for i in range(len(num_lst)):
        if start <= num_lst[i] <= end:
            indexes_list.append(i)
    return indexes_list