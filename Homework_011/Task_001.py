# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения, сложения, *умножения матриц

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        rows = []
        for row in self.matrix:
            row_str = "\t".join(str(element) for element in row)
            rows.append(row_str)
        return "\n".join(rows)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return False

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                raise ValueError("Матрицы должны иметь одинаковый размер для сложения.")
            result = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[i])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(row)
            return Matrix(result)
        raise ValueError("Можно складывать только матрицы.")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if len(self.matrix[0]) != len(other.matrix):
                raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
            result = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(other.matrix[0])):
                    element = 0
                    for k in range(len(other.matrix)):
                        element += self.matrix[i][k] * other.matrix[k][j]
                    row.append(element)
                result.append(row)
            return Matrix(result)
        raise ValueError("Матрицы можно умножать только на матрицы.")


# Пример использования:
m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 9 , 3]])
m2 = Matrix([[7, 8, 3], [9, 10, 7], [11, 12, 13]])

print("Матрица 1:")
print(m1)
print()

print("Матрица 2:")
print(m2)
print()

print("Сложение матриц:")
print(m1 + m2)
print()

print("Умножение матриц:")
print(m1 * m2)
print()

print("Сравнение матриц:")
print(m1 == m2)
