print('Задача 12: \n'
'Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.\n'
'Петя помогает Кате по математике. Он задумывает два натуральных \n'
'числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя\n'
'делает две подсказки. Он называет сумму этих чисел S и их произведение P.\n'
'Помогите Кате отгадать задуманные Петей числа.')

print('4 4 -> 2 2')
print('5 6 -> 2 3')

# var 1

num_sum = int(input('Введите сумму двух чисел: '))
num_product = int(input('Введите произведение двух чисел: '))

c = 0
for i in range(num_sum):
    if c:
        break
    for j in range(num_product):
        if i + j == num_sum and i * j == num_product:
            print(f'{num_sum} {num_product} -> {j} {i}')
            print()

# var 2
# способ через математику

num_sum = int(input('Введите сумму двух чисел: '))
num_product = int(input('Введите произведение двух чисел: '))

x = int((num_sum + (num_sum ** 2 - 4 * num_product) ** 0.5) / 2)
y = int((num_sum - (num_sum ** 2 - 4 * num_product) ** 0.5) / 2)
print(f'{num_sum} {num_product} -> {x} {y}')