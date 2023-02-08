"""Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов."""

from random import uniform
num_list = [round(uniform(0, 10), 2) for _ in range(int(input('Введите размер списка: ')))]
print(*num_list)
digits_list = []
for num in num_list:
    # добавляем в список числа, стоящие после запятой
    digits_list.append(int(str(num)[int(str(num).find('.') + 1): len(str(num))]))
print(*digits_list)
print(max(digits_list) - min(digits_list))