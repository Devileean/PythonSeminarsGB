print('Задача 19. \n '
'Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность \n '
'(сдвиг - циклический) на K элементов вправо, K – положительное число.\n ')


from random import randint
num_list = [randint(0, 10) for _ in range(int(input('Введите размер списка: ')))]
print(*num_list)
offset = int(input('Введите размер сдвига: '))
if offset > len(num_list):
    offset %= len(num_list)
print(num_list[offset:] + num_list[:offset])