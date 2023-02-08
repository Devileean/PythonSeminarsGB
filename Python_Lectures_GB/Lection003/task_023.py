print('Задача 23. \n'
'Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество \n'
'элементов массива, больших предыдущего (элемента с предыдущим номером) \n')

from random import randint
num_list = [randint(-10, 10) for _ in range(int(input('Введите размер списка: ')))]
count = 0
for i in range(1, len(num_list)):
    if num_list[i] > num_list[i - 1]:
        count += 1
print(*num_list)
print(f'Количество элементов, больших предыдущего, равно {count}')