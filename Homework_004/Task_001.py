# Напишите функцию для транспонирования матрицы

import random

def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transposed_matrix = [[0 for _ in range(rows)] for _ in range(columns)]

    for i in range(rows):
        for j in range(columns):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

def generate_random_3x3_matrix():
    matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
    
    return matrix

matrix = generate_random_3x3_matrix()
transposed = transpose_matrix(matrix)

print("Исходная матрица:")
for row in matrix:
    print(row)

print("Транспонированная матрица:")
for row in transposed:
    print(row)
