# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например,
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

class MatrixSizeError(Exception):
    def __init__(self, message="Матрицы должны иметь одинаковый размер для операции."):
        super().__init__(message)


class MatrixMultiplicationError(Exception):
    def __init__(self, message="Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы."):
        super().__init__(message)


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
                raise MatrixSizeError()
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
                raise MatrixMultiplicationError()
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
m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 9, 3]])
m2 = Matrix([[7, 8, 3], [9, 10, 7], [11, 12, 13]])

print("Матрица 1:")
print(m1)
print()

print("Матрица 2:")
print(m2)
print()

try:
    print("Сложение матриц:")
    print(m1 + m2)
    print()
except MatrixSizeError as e:
    print(f"Ошибка при сложении матриц: {e}")
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    print("Умножение матриц:")
    print(m1 * m2)
    print()
except MatrixMultiplicationError as e:
    print(f"Ошибка при умножении матриц: {e}")
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    print("Сравнение матриц:")
    print(m1 == m2)
except ValueError as e:
    print(f"Ошибка: {e}")
