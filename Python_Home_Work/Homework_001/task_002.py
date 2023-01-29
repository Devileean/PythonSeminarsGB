# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
print("Задача 2: Найдите сумму цифр трехзначного числа.")
try:
    any_num = int(input("введите любое трехзначное число: "))
except:
    print("введён текст")

if 100 <= any_num <= 999:
    first_num = any_num // 100
    second_num = any_num // 10 % 10
    third_num = any_num % 10

    summa = first_num + second_num + third_num

    print(f"{any_num} -> {summa} ({first_num} + {second_num} + {third_num})")

else:
    print("вы ввели не верное число")
