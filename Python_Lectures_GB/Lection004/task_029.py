# # Ваня
# n = int(input())
# max_number = 1000   # 1
# while n != 0:
#     n = int(input())
#     if max_number > n:   # 2
#         max_number = n
# print(max_number)


# # Петя
# n = int(input())
# max_number = -1   #1
# while n < 0:   #2
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n)   #3

# Ira
n = int(input())
max_number = n   # 1
while n != 0:
    n = int(input())
    if max_number < n:   # 2
        max_number = n
print(max_number)