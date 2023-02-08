# 1. Сумма трёх.
print('Посчитайте сумму трёх введённых чисел.')
# 1 + 2 + 3 = 6

number1 = int(input('введите первое чесло: '))
number2 = int(input('введите второе чесло: '))
number3 = int(input('введите третье чесло: '))

summa = number1 + number2 + number3

print(f'{number1} + {number2} + {number3} = {summa}')

# 2. Площадь.
print('Пользователь вводит стороны прямоугольника, выведите его площадь.')

side_a = float(input('введите первую сторону прямоугольника: '))
side_b = float(input('введите вторую сторону прямоугольника: '))
square = side_a * side_b
print(f'площадь прямоугольника введенных сторон -> {square}')

# 3. Периметр.
print('Пользователь вводит стороны прямоугольника, выведите его периметр.')

side_c = float(input('введите первую сторону прямоугольника: '))
side_d = float(input('введите вторую сторону прямоугольника: '))
perimeter = (side_c + side_d) * 2
print(f'периметер прямоугольника введенных сторон -> {perimeter}')

##########################################################################################################
# У # C # Л # О # В # И # Е #

# 1. Меньшее из двух.
print('Пользователь вводит два целых числа. Выведите меньшее из них.')

number_one = int(input('введите первое число: '))
number_two = int(input('введите второе число: '))

if number_one > number_two:
    print(f'это число большее {number_one}')
elif number_one == number_two:
    print(f'{number_one} и {number_two} равны')
else:
    print(f'это число большее {number_two}')

# 2. Четырёхзначное?


print('Пользователь вводит целое число. Выведите YES, если это число является чётырёхзначным, и NO в противном случае.')

# Способ 1:
any_number = int(input('введите любое число: '))

if 1000 <= any_number < 10000:
    print('YES')
else:
    print('NO')

# Способ 2:

any_string_number = input('введите любое число: ')

if '-' in any_string_number:
    if len(any_string_number) == 5:
        print('YES')
    else:
        print('NO')
else:
    if any_string_number == 4:
        print('YES')
    else:
        print("NO")


"""Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции."""

from random import randint
num_list = [randint(0, 10) for _ in range(int(input('Введите размер списка: ')))]
elements_sum = 0
for i in range(1, len(num_list), 2):
    elements_sum += num_list[i]
print(*num_list)
print(elements_sum)

"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д."""

from random import randint
num_list = [randint(0, 10) for _ in range(int(input('Введите размер списка: ')))]
pairs_sum = []
start, end = 0, -1
for _ in range(len(num_list) // 2):
    pairs_sum.append(num_list[start] * num_list[end])
    start += 1
    end -= 1
if len(num_list) % 2 == 1:
    pairs_sum.append(num_list[len(num_list) // 2] ** 2)
print(*num_list)
print(*pairs_sum)

"""Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов."""

from random import uniform
num_list = [round(uniform(0, 10), 2) for _ in range(int(input('Введите размер списка: ')))]
print(*num_list)
digits_list = []
for num in num_list:
    # добавляем в список числа, стоящие после запятой
    digits_list.append(int(str(num)[int(str(num).find('.') + 1): len(str(num))]))
print(*digits_list)
print(max(digits_list) - min(digits_list))

"""Напишите программу, которая будет преобразовывать десятичное число в двоичное."""

# var 1 - склеить число через join
user_num = int(input('Введите целое положительное число: '))
user_num_copy = user_num
bin_list = []
while user_num_copy // 2 != 0:
    bin_list.append(str(user_num_copy % 2))
    user_num_copy //= 2
bin_list.append(str(user_num_copy % 2))
bin_num = int(''.join(reversed(bin_list)))
print(f'{user_num} -> {bin_num}')

#var 2 - вывести распакованный список без пробелов
user_num = int(input('Введите целое положительное число: '))
user_num_copy = user_num
bin_list = []
while user_num_copy // 2 != 0:
    bin_list.append(user_num_copy % 2)
    user_num_copy //= 2
bin_list.append(user_num_copy % 2)
print(f'{user_num} ->', end=' ')
print(*reversed(bin_list), sep='')

"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов."""

size = int(input('Введите длину последовательности: '))
fibo_nums = [0, 1]
negafibo_nums = [1, -1]
for i in range(2, size + 1):
    fibo_nums.append(fibo_nums[i - 2] + fibo_nums[i - 1])
for j in range(2, size):
    negafibo_nums.append(negafibo_nums[j - 2] - negafibo_nums[j - 1])
negafibo_nums.reverse()
#negafibo_nums.extend(fibo_nums)
negafibo_nums += fibo_nums
print(*negafibo_nums)
