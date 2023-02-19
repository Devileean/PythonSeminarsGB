print("""Задача 45.
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не превосходящее 10^5. Программа должна вывести все
пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
пару не дает). """)

from module import friendly_nums

friendly_nums(int(input('Введите верхнюю границу: ')))

def sum_divisors(num):
    summ = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            # print(f'{i = }')
            summ += i
    return summ


def friends_num(number):
    for i in range(1, number):
        j = sum_divisors(i)
        if i < j <= number and i == sum_divisors(j):
            print(i, j)


friends_num(int(input('Введите число К: ')))