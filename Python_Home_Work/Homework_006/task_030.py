print("""Задача 30.
Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
an  = a1  + (n-1) * d. Каждое число вводится с новой строки.""")

from defs_homework_6 import arithmetic_sequence

first_element = int(input('Введите первый элемент: '))
element_diff = int(input('Введите разность между элементами: '))
quantity_elements = int(input('Введите количество элементов: '))
print(*arithmetic_sequence(first_element, element_diff, quantity_elements))
