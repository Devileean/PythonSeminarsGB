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
