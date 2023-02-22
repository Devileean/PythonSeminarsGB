def find_rhythm(text: str):
    phrases = text.split()   # разбили текст на фразы
    phrases_vow = []   # пустой список для фраз, очищенных от согласных
    for i in phrases:   # каждую фразу фильтруем от согласных
        phrases_vow.append(list(filter(lambda x: x in 'аеиоуэюя', list(i))))
    result_list = map(lambda x: len(x) == len(phrases_vow[0]), phrases_vow)
    return all(result_list)

# вариант с генератором списка и построчным выводом матрицы
def print_operation_table(operation, num_rows=6, num_columns=6):
    # генерируем двумерную матрицу
    matrix = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    # построчно распечатываем матрицу
    for x in range(num_rows):
        temp = []
        for y in range(num_columns):
            temp.append(str(matrix[x][y]).ljust(3))
        print(*temp)

# вариант с поэлементным выводом матрицы
def print_operation_table1(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(str(operation(i, j)).ljust(3), end=' ')
        print()

