"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов."""

size = int(input('Введите длину последовательности: '))
fibo_nums = [0, 1]
negafibo_nums = [1, -1]
for i in range(2, size + 1):
    fibo_nums.append(fibo_nums[i - 2] + fibo_nums[i - 1])
for j in range(2, size):
    negafibo_nums.append(negafibo_nums[j - 2] - negafibo_nums[j - 1])
negafibo_nums.reverse()
#negafibo_nums.extend(fibo_nums)
negafibo_nums += fibo_nums
print(*negafibo_nums)