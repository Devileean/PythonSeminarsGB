# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
initial_list = [randint(0, 10) for _ in range(int(input('Введите длину последовательности: ')))]
print(*initial_list)
unique_nums = set(initial_list)
print('Неповторяющиеся элементы последовательности: ', *unique_nums)