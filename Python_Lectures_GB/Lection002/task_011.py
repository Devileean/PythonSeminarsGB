print('Задача 11. \n'
'Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, \n'
'то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1 \n')

# var1
"""user_input = int(input('Введите целое положительное число: '))
fibo_nums = [0, 1]
n = fibo_nums[1]
while n < user_input:
    n = fibo_nums[-1] + fibo_nums[-2]
    fibo_nums.append(n)
if user_input in fibo_nums:
    print(f'{user_input} - число Фиббоначи №{fibo_nums.index(user_input) + 1}')
else:
    print(f'{user_input} не является числом Фиббоначи')"""

# var 2
user_input = int(input('Введите целое положительное число: '))
n1, n2 = 0, 1
n_num = 2
while n2 < user_input:
    n1, n2 = n2, n1 + n2
    n_num += 1
if n2 == user_input:
    print(f'{user_input} - число Фиббоначи №{n_num}')
else:
    print(f'{user_input} не является числом Фиббоначи')