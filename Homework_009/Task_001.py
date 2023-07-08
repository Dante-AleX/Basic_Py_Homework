# Напишите следующие функцию нахождения корней квадратного уравнения

# Находит корни квадратного уравнения вида ax^2 + bx + c = 0.

    # Параметры:
    #     a (float): коэффициент при x^2.
    #     b (float): коэффициент при x.
    #     c (float): свободный член.
import math

def solve_equation(a, b, c):
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

a = float(input('Please insert the first coefficient: '))
b = float(input('Please insert the second coefficient: '))
c = float(input('Please insert the third coefficient: '))

result = solve_equation(a, b, c)
if result == (None, None):
    print('Delta is lower than 0')
else:
    x1, x2 = result
    print(f'The result roots for the {a}x^2+{b}x+{c}=0 equation are {x1:.2f} and {x2:.2f}')
