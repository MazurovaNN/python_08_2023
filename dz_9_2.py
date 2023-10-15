# 2. Пакет для работы с файлами 3
# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

# Создайте файл __init__.py и запишите в него все функции:
# save_to_json,
# find_roots,
# generate_csv_file.



code_to_write = '''
import csv
import json
import random

def save_to_json(func):
    def wrapper(*args):
        result_list = []
        with open(args[0], 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                data = {'parameters': [a, b, c], 'result': result}
                result_list.append(data)
        with open('results.json', 'w') as f:
            json.dump(result_list, f)
    return wrapper

@save_to_json
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)