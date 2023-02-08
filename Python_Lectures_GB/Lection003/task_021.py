print('Задача №21. \n'
'Напишите программу для печати всех уникальных значений в словаре. \n '
'Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, \n '
'{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII \n '
'":" S007 "}] \n ')

user_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": " S005 "}, {"VII": "S005"},
             {"V":" S009 "}, {" VIII": "S007"}]
values = set()
for i in range(len(user_dict)):
    for value in user_dict[i].values():
        values.add(value.strip())
print(f'Множество уникальных значений: {values}')