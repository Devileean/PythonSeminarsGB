print('Задача 25. \n'
'Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ \n '
'уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n. \n')

line = [i for i in input().split()]
letters, new_line = {}, []
for letter in set(line):
    letters.setdefault(letter, 0)
for s in line:
    if letters[s] == 0:
        new_line.append(s)
        letters[s] += 1
    else:
        new_line.append(f'{s}_{letters[s]}')
        letters[s] += 1
print(*new_line)