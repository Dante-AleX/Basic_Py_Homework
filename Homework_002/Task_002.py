# Напишите программу, которая принимает две строки вида “a/b” - 
# дробь с числителем и знаменателем. Программа должна возвращать 
# сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def calc (frac1, frac2):
    sum_frac = frac1 + frac2
    product_frac = frac1 * frac2
    return sum_frac, product_frac

frac1_str = input("Введите первую дробь (в формате a/b): ")
frac2_str = input("Введите вторую дробь (в формате a/b): ")

frac1_parts = frac1_str.split("/")
frac2_parts = frac2_str.split("/")

if len(frac1_parts) != 2 or len(frac2_parts) != 2:
    print("Некорректный ввод. Пожалуйста, используйте формат a/b.")
    exit()

numerator1 = int(frac1_parts[0])
denominator1 = int(frac1_parts[1])
numerator2 = int(frac2_parts[0])
denominator2 = int(frac2_parts[1])

frac1 = Fraction(numerator1, denominator1)
frac2 = Fraction(numerator2, denominator2)

sum_frac, product_frac = calc(frac1, frac2)

print("Сумма дробей:", sum_frac)
print("Произведение дробей:", product_frac)
