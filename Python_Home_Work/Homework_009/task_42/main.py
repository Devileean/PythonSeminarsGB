import csv

print("""Задача 42. 
Узнать какая максимальная households в зоне минимального значения population"""
      )

with open("../simple_data/california_housing_train.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    array_pop = {}
    counter = 0
    for row in reader:
        if int(float(row['population'])) <= 500:
            array_pop[counter] = (int(float(row['population'])))
            counter += 1
    print(max(array_pop), "<-- максимальная households в зоне минимального значения population")