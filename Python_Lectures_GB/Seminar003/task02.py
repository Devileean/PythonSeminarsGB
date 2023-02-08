"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д."""

from random import randint
num_list = [randint(0, 10) for _ in range(int(input('Введите размер списка: ')))]
pairs_sum = []
start, end = 0, -1
for _ in range(len(num_list) // 2):
    pairs_sum.append(num_list[start] * num_list[end])
    start += 1
    end -= 1
if len(num_list) % 2 == 1:
    pairs_sum.append(num_list[len(num_list) // 2] ** 2)
print(*num_list)
print(*pairs_sum)