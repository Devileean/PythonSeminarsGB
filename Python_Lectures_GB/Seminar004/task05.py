# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
with open('file1.txt', 'r') as file_1:
    polynom_1 = file_1.readline()
with open('file2.txt', 'r') as file_2:
    polynom_2 = file_2.readline()
with open('result.txt', 'w') as result_file:
    result_file.write(f'{polynom_1} + {polynom_2} = {polynom_1 + polynom_2}')