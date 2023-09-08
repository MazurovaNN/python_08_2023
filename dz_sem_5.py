# 1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)

# 2. Напишите однострочный генератор словаря, который принимает на вход три списка 
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

def generate_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}

names = ["Alex", "Boby", "Clear"]
salaries = [15000, 17000, 20000]
bonuses = ["15%", "17%", "20%"]

salary_dict = generate_salary_dict(names, salaries, bonuses)
print(salary_dict)

# 3. Создайте функцию генератор чисел Фибоначчи (см. Википедию).
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

     
