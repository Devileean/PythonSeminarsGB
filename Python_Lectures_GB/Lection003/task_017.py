print('Задача 17.\n'
'Дан список чисел. Определите, сколько в нем встречается различных чисел.')

from random import randint
num_list = [randint(0, 10) for _ in range(int(input('Введите размер списка: ')))]
print(*num_list)
print(f'Количество различных чисел в списке = {len(set(num_list))}')