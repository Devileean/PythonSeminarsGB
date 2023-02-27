import csv

print("""Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)"""
      )
with open("../simple_data/california_housing_train.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        if int(float(row['population'])) <= 500:
            print(int(float(row['population'])), '<--популяция | средняя стоимость дома -->',
                  int(float(row['median_house_value'])))
