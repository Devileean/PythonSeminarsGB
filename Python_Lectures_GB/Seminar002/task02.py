"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)"""

user_input = int(input('Введите число: '))
num_product_list = [1]
product = 1
for i in range(2, user_input + 1):
    product *= i
    num_product_list.append(product)
print(*num_product_list)