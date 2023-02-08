# Вычислить число c заданной точностью d
from decimal import Decimal
d = Decimal(input('Введите точность округления: '))
num_round = Decimal(input('Введите число: '))
print(num_round.quantize(d))