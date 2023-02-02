print('Задача 14:\n'
'Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.')

print('10 -> 1 2 4 8')

any_number = int(input("Введите число: "))
m = 1

print(f'{any_number} -> ')

while m < any_number:

    print(m, end=' ')
    m = m * 2


