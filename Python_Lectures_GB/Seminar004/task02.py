"""Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N."""

def num_is_prime(x):
    count = 0
    for f in range(1, x + 1):
        if x % f == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


user_num = int(input('Введите число: '))
factor_list = []
for i in range(2, user_num + 1):
    if user_num % i == 0 and num_is_prime(i):
        factor_list.append(i)
print(*factor_list)