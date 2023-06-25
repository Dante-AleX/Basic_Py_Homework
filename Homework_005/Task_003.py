# Создайте функцию генератор чисел Фибоначчи

def fibonacci(limit):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= limit:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

limit = 1000
fib_nums = fibonacci(limit)
print(fib_nums)
