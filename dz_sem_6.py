# 1.В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
 
# import argparse
# from module_data_dz6 import datetime  # из отдельного модуля module_data_dz6.py

# def validate_date(date):
#     try:
#         datetime.strptime(date, '%Y-%m-%d')
#         return True
#     except ValueError:
#         return False

# parser = argparse.ArgumentParser(description='Check date.')
# parser.add_argument('date', type=str, help='Date to check in the format YYYY-MM-DD')

# args = parser.parse_args()

# print(validate_date(args.date))


# 2.Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу
# о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
 
def validate_queens(positions): # находится в модуле module1_dz6.py
    for i in range(8):
        for j in range(i+1, 8):
            # проверка на наличие на одной строке или диагонали
            if positions[i] == positions[j] or \
                positions[i] - i == positions[j] - j or \
                positions[i] + i == positions[j] + j:
                return False
    return True

# 3.Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random
from module1_dz6 import validate_queens

def generate_positions():
    positions = list(range(1, 9))  # создаём список с числами от 1 до 8
    for i in range(4):  # 4 успешные расстановки
        random.shuffle(positions)  # перемешиваем список
        while not validate_queens(positions):  # если расстановка не успешная, перемешиваем ещё раз
            random.shuffle(positions)
        print(positions)  # выводим успешную расстановку