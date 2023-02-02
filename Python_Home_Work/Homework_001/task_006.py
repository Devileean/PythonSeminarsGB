print(' Задача 6: \n'
      'Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали \n'
      'билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма \n'
      'первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. \n'
      '3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.')

print('385916 -> yes')
print('123456 -> no')

# Первый способ
# ticket_number = str(input('Введите шестизначный номер билета: '))
#
# if len(ticket_number) <= 5 or len(ticket_number) >= 7:
#     print('Вы ввели не верный номер!')
# else:
#     sum1 = int(ticket_number[0])+int(ticket_number[1])+int(ticket_number[2])
#     sum2 = int(ticket_number[3])+int(ticket_number[4])+int(ticket_number[5])
#
# if sum1 == sum2:
#     print(f'{ticket_number} -> yes')
# else:
#     print(f'{ticket_number} -> no')

# Второй способ

# try:
#     ticket_number = int(input('Введите шестизначный номер билета: '))
# except:
#     print('Ввели текст')
# if 99999 < ticket_number < 1000000:
#     first_three_num, end_three_num = 0, 0
#     ticket = ticket_number
#     for i in range(6):
#         if i > 2:
#             first_three_num += ticket_number % 10
#         else:
#             end_three_num += ticket_number % 10
#         ticket_number = int(ticket_number / 10)
#     if first_three_num == end_three_num:
#         print(f'{ticket} -> yes')
#     else:
#         print(f'{ticket} -> no')
# else:
#     print('Вы ввели не верный номер!')

# Третий способ

lucky_ticket = int(input('Введите шестизначный номер билета: '))
a = lucky_ticket // 10 ** 5
b = lucky_ticket % 10 ** 5 // 10 ** 4
c = lucky_ticket % 10 ** 4 // 10 ** 3
d = lucky_ticket % 10 ** 3 // 10 ** 2
e = lucky_ticket % 10 ** 2 // 10
f = lucky_ticket % 10
print(a + b + c == d + e + f)
