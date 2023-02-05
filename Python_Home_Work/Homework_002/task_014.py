print('Задача 14:\n'
'Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.')

print('10 -> 1 2 4 8')

# # var1 без списка
# any_num = int(input('Введите целое положительное число: '))
# two_pow, power = 1, 1
# while two_pow <= any_num:
#     print(two_pow, end=' ')
#     two_pow = 2 ** power
#     power += 1

# var2 со списком
any_num = int(input('Введите целое положительное число: '))
print_any_num = any_num
two_pow_list = []
two_pow, power = 1, 1
while two_pow <= any_num:
    two_pow_list.append(two_pow)
    two_pow = 2 ** power
    power += 1
print(any_num, " -> ", *two_pow_list)

