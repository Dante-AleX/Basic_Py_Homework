# Напишите функцию декоратор, запускающий функцию нахождения корней 
# квадратного уравнения с каждой тройкой чисел из csv файла.

import csv
import math

def solve_equation(a, b, c):
    if a == 0:
        return None, None

    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        x = -b / (2 * a)
        return x, None
    else:
        return None, None

def process_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        for row in reader:
            try:
                a, b, c = map(float, row)
                result = solve_equation(a, b, c)
                if result is not None:
                    print(f"For {a}x^2 + {b}x + {c} = 0, the roots are: {result}")
                else:
                    print(f"Invalid equation with a = 0: {a}x^2 + {b}x + {c}")
            except ValueError:
                print(f"Invalid row: {row}")

def quadratic_equation_solver_decorator(func):
    def wrapper(filename):
        print(f"Running quadratic equation solver for each row in {filename}...")
        func(filename)
        print("Quadratic equation solver completed.")
    return wrapper

@quadratic_equation_solver_decorator
def solve_equations(filename):
    process_csv(filename)

filename = r'D:\Academy\Geek Brains\Лекции\Python\Основы Python\Basic_Py_Homework\Homework_009\input.csv'
solve_equations(filename)
