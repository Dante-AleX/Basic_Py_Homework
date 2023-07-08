# Напишите функцию, которая получает на вход директорию и 
# рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.

# 1) Для дочерних объектов указывайте родительскую директорию.
# 2) Для каждого объекта укажите файл это или директория.
# 3) Для файлов сохраните его размер в байтах, 
#    а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

def inspect_folder(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        dir_size = 0
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            dir_size += size
            result.append({'path': file_path, 'type': 'file', 'size': size, 'parent_directory': root})
        result.append({'path': root,'type': 'directory','size': dir_size,'parent_directory': os.path.dirname(root)})
    with open('result.json', 'w') as json_file:
        json.dump(result, json_file, indent=1)
    with open('result.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['path', 'type', 'size', 'parent_directory'])
        writer.writeheader()
        writer.writerows(result)
    with open('result.pickle', 'wb') as pickle_file:
        pickle.dump(result, pickle_file)


if __name__ == '__main__':
    # Введите свою директорию вместо слова "Директория"
    inspect_folder(r'Директория')
