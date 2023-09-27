# 1. Решить задания, которые не успели решить на семинаре.

# 2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит 
#её и все вложенные директории. Результаты обхода сохраните 
# в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов 
# в ней с учётом всех вложенных файлов и директорий. 

# 3. Соберите из созданных на уроке и в 
# рамках домашнего задания функций пакет для работы с файлами разных форматов.

import os       # импортируем
import json
import csv
import pickle

def get_size(path):   # функция
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total

def directory_walker(dir_path):   # функция 
    results = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root, 
                            "is_file": True,
                            "name": name,
                            "size_in_bytes": os.path.getsize(full_path)})

        for name in dirs:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root, 
                            "is_file": False,
                            "name": name,
                            "size_in_bytes": get_size(full_path)})

    with open("output.json", "w") as json_file:   # файл json
        json.dump(results, json_file)

    with open("output.csv", "w") as csv_file: # файл csv
        writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    with open("output.pickle", "wb") as pickle_file:  # файл pickle
        pickle.dump(results, pickle_file)

directory_walker("./my_folder")
