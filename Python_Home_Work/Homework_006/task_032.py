print("""Задача 32.
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного максимума) """)

from defs_homework_6 import create_list, indexes_of_numbers

num_list = create_list(int(input('Введите размер массива: ')))
left_endpoint = int(input('Введите MIN диапазона: '))
right_endpoint = int(input('Введите MAX диапазона: '))

print(*num_list)
print(*indexes_of_numbers(num_list, left_endpoint, right_endpoint))