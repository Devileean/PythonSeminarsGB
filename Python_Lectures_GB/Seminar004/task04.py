"""Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени k."""

from random import randint
power = int(input('Введите значение степени: '))
coefficients = [randint(0, 10) for _ in range(power + 1)]
print(coefficients)
terms = []
for i in range(power, -1, -1):
    if coefficients[len(coefficients) - i - 1] == 0:
        continue
    if i == 0:
        terms.append(f'{coefficients[len(coefficients) - i - 1]}')
    elif i == 1:
        terms.append(f'{coefficients[len(coefficients) - i - 1] if coefficients[len(coefficients) - i - 1] != 1 else ""}x')
    else:
        terms.append(f'{coefficients[len(coefficients) - i - 1] if coefficients[len(coefficients) - i - 1] != 1 else ""}x**{i}')
print(' + '.join(terms))