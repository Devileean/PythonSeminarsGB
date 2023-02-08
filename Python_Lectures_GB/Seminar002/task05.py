# Реализуйте алгоритм перемешивания списка.

# var1 Перемешивает исходный список на месте
import random as r
elements = [r.randint(0,  100) for _ in range(int(input('Введите кол-во элементов в списке: ')))]
print('Исходный список:', *elements)
r.shuffle(elements)
print('Перемешанный список № 1:', *elements)

# var 2 Выдает случайную выборку такую же по размеру как исходный список
print('Перемешанный список № 2:', *r.sample(elements, len(elements)))

# var 3 Переносит случайным образом элементы из исходного списка в новый
elements_new = []
count = len(elements)
for _ in range(len(elements)):
    elements_new.append(elements.pop(r.randrange(count)))
    count -= 1
print('Перемешанный список № 3:', *elements_new)