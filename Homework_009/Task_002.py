# Напишите функцию генерации csv файла 
# с тремя случайными числами в каждой строке. 100-1000 строк.

import csv
import random

def generate_csv(filename, rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Number 1', 'Number 2', 'Number 3'])  # Записываем заголовок

        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]  # Генерируем случайные числа
            writer.writerow(row)

filename = 'random_numbers.csv'
rows = random.randint(100, 1000)

generate_csv(filename, rows)
print(f'CSV file "{filename}" with {rows} rows has been generated.')
