print(' Задача 6: \n'
'Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали \n'
'билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма \n'
'первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. \n'
'3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.')

print('385916 -> yes')
print('123456 -> no')

ticket_number = str(input('Введтите шестизначный номер билета: '))

if len(ticket_number) <= 5 or len(ticket_number) >= 7:
    print('Вы ввели не верный номер!')
else:
    sum1 = int(ticket_number[0])+int(ticket_number[1])+int(ticket_number[2])
    sum2 = int(ticket_number[3])+int(ticket_number[4])+int(ticket_number[5])

if sum1 == sum2:
    print(f'{ticket_number} -> yes')
else:
    print(f'{ticket_number} -> no')