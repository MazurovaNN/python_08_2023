# 1
# a = 5
# b = 3.6
# c = 's'
# print(type(a))
# print(type(b))
# print(type(c))

# 2
# data = [1, 0.5, 's']
# for e, item in enumerate(data, start=1):
#     print(e, item, id(e), item.__sizeof__(), hash(item), 'целое' if isinstance(item, int) else '',
#            'строка' if isinstance(item, str) else '' )


# 3
# def binary(a: int, b: int)->str: 
#     res = ''
#     while a > 0:
#         res = str(a % b) + res
#         a = a // b
#     return res

# a: int = int(input('Введите значение '))
# b: int = int(input('Введите систему исчисления '))
# print(binary(a, b))
# print(bin(a))
# print(oct(a))

# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# import decimal
# import math

# STOP_DIAMETR = 1000
# decimal.getcontext().prec = 50
# diametr = decimal.Decimal(input('Введите диаметр окружности:  '))


# if diametr <= STOP_DIAMETR:
#     square = decimal.Decimal(math.pi) * (diametr/2)**2
#     print(square)
#     line = decimal.Decimal(math.pi) * diametr
#     print(line)
# else:
#     print('Вы ввели число вне диапозона')

    # 5 
a = 5
b = 10
c = -2

D = complex(b**2 - 4*a*c, 0)
x1 = (-b + D**0.5)/(2*a)
x2 = (-b - D**0.5)/(2*a)
print(D, x1, x2)