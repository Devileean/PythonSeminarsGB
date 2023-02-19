def create_list(x: int):
    my_list = []
    for _ in range(x):
        my_list.append(int(input('Введите число: ')))
    return my_list


def list_diff(lst1: list, lst2: list):
    new_list = []
    for i in lst1:
        if i not in lst2:
            new_list.append(i)
    return new_list


def max_of_3(num_list: list):
    count = 0
    for i in range(1, len(num_list) - 1):
        if num_list[i - 1] < num_list[i] and num_list[i + 1] < num_list[i]:
            print(num_list[i], end=' ')
            count += 1
    print()
    return count


def count_pairs(lst: list):
    return sum([lst.count(i) // 2 for i in set(lst)])


def sum_of_div(n):
    sum_div = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum_div += i
    return sum_div


def friendly_nums(num: int):
    skip = None
    for j in range(2, num):
        if j == skip:
            continue
        sum_j = sum_of_div(j)
        for k in range(2, num):
            if k == j:
                continue
            if k == sum_j:
                if j == sum_of_div(k):
                    print(j, k)
                    skip = k