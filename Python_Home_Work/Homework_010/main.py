import pandas as pd
import random

lst = ['robot'] * 10 # генерирую список робота
lst += ['human'] * 10 # генерирую список человека
random.shuffle(lst) # перемешиваем хуман и робот
data = pd.DataFrame({'whoAmI': lst}) # создает табличку в один столбик

data['robot'] = data # мы берем столбик  whoami и копируем в столбик робота
data = data.rename({"whoAmI": "human"}, axis='columns') # переименовываем столбик whoami в хуман
data['human'] = data['human'].replace('robot', '0')
data['human'] = data['human'].replace('human', '1')
data['robot'] = data['robot'].replace('robot', '1')
data['robot'] = data['robot'].replace('human', '0')
data.head()
data.to_csv('saved_task.csv', index=False) # сохраняем всё в файл saved_task.csv