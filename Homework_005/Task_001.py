# Напишите функцию, которая принимает на вход строку — 
# абсолютный путь до файла. Функция возвращает кортеж из трёх 
# элементов: путь, имя файла, расширение файла.

import os

def parse_file_path(file_path):
    path = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    filename, extension = os.path.splitext(filename)
    return path, filename, extension

file_abs = r"D:\Documents\CV - Eng\example.txt"
result = parse_file_path(file_abs)
print(result)

