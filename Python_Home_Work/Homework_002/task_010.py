print('Задача 10: \n'
'На столе лежат n монеток. Некоторые из них лежат вверх решкой, \n'
'а некоторые – гербом. Определите минимальное число монеток, \n'
'которые нужно перевернуть, чтобы все монетки были повернуты \n'
'вверх одной и той же стороной. Выведите минимальное количество \n'
'монет, которые нужно перевернуть.')

print('5 -> 1 0 1 1 0')


# var 1 - без коллекций
from random import randint # Возвращает случайное число в пределах заданного промежутка
coin_num = int(input('Введите количество монеток: '))
print_coins = coin_num
eagle_num, tail_num = 0, 0
for _ in range(coin_num):
    coin = randint(0, 1)
    print(coin, end=' ')
    if coin == 0:
        eagle_num += 1
    else:
        tail_num += 1
print()
if eagle_num == tail_num:
    print(f'Монеты можно не переворачивать, их кол-во одинаковое и равное {eagle_num}')
elif eagle_num < tail_num:
    print(f'Переверните монеты с орлом {eagle_num} раз(а)')
else:
    print(f'Переверните монеты с решкой {tail_num} раз(а)')

# #var2 через кортеж
# from random import randint
# coins = tuple(randint(0, 1) for _ in range(int(input('Введите количество монеток: '))))
# print_coins = coins
# print(*coins)
# eagle_num = coins.count(0)
# tail_num = coins.count(1)
# if eagle_num == tail_num:
#     print(f'Монеты можно не переворачивать, их кол-во одинаковое и равное {eagle_num}')
# elif eagle_num < tail_num:
#     print(f'Переверните монеты с орлом {eagle_num} раз(а)')
# else:
#     print(f'Переверните монеты с решкой {tail_num} раз(а)')
