"""Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции."""

from random import randint
num_list = [randint(0, 10) for _ in range(int(input('Введите размер списка: ')))]
elements_sum = 0
for i in range(1, len(num_list), 2):
    elements_sum += num_list[i]
print(*num_list)
print(elements_sum)