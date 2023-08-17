'''
Напишите программу, которая вычисляет площадь круга и длину окружности по
введённому диаметру.
Диаметр не превышает 1000 у.е.
Точность вычислений должна
составлять не менее 42 знаков после запятой.
'''
import decimal
import math

DIAMETR = 1000
AССURACY = 50
decimal.getcontext().prec = AССURACY
diameter = decimal.Decimal(input('Введите диаметр окружности: '))

if diameter <= DIAMETR:
    square = decimal.Decimal(math.pi)*(diameter/2)**2
    print(square)
    line = decimal.Decimal(math.pi)*diameter
    print(line)
else:
    print('Введено число вне диапазона, 1000')
