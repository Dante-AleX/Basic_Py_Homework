import doctest
import unittest
import pytest

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

class MatrixTestCase(unittest.TestCase):
    def test_matrix_addition(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1 + m2
        self.assertEqual(str(result), "6\t8\n10\t12")

    def test_matrix_multiplication(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1 * m2
        self.assertEqual(str(result), "19\t22\n43\t50")

    def test_matrix_equality(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2], [3, 4]])
        self.assertTrue(m1 == m2)

    def test_matrix_inequality(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        self.assertTrue(m1 != m2)
def test_matrix_addition():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    result = m1 + m2
    assert str(result) == "6\t8\n10\t12"

def test_matrix_multiplication():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    result = m1 * m2
    assert str(result) == "19\t22\n43\t50"

def test_matrix_equality():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2], [3, 4]])
    assert m1 == m2

def test_matrix_inequality():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    assert m1 != m2


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite())
    return tests

if __name__ == '__main__':
    # Запуск PyTest
    pytest.main([__file__])

    # Запуск UnitTest
    unittest.main()

    # Запуск DocTest
    unittest.TestLoader().loadTestsFromModule(__name__)
