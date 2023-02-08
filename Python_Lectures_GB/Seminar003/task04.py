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