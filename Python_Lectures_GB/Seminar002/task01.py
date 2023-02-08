"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""

# var1 - через строки
s = input('Введите любое число: ')
digit_sum = 0
for i in range(len(s)):
    if s[i].isdigit():
        digit_sum += int(s[i])
print(digit_sum)


# var2 - через десятичные числа
from decimal import *
user_num = abs(Decimal(input('Введите любое число: ')))
digits_sum = 0
for digit in user_num.as_tuple().digits:
    digits_sum += digit
print(digits_sum)

# var3
user_input = input('Введите любое число: ')
# 1) переводим строку в float, 2) берем от нее модуль,
# 3) домножаем на 10 в степени длина строки, чтобы гарантированно перенести все цифры в целую часть
# 4) переводим float в int
user_num = int(abs(float(user_input)) * 10 ** (len(str(user_input))))
digits_sum = 0
while user_num > 0:
    digits_sum += user_num % 10
    user_num //= 10
print(digits_sum)