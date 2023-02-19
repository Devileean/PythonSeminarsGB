def arithmetic_sequence(first_element: int, element_diff: int, quantity_elements:int):
    sequence = [first_element]
    for i in range(2, quantity_elements + 1):
        sequence.append(first_element + (i - 1) * element_diff)
    return sequence


