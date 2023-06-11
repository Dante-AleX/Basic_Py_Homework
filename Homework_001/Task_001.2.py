# Написать порграмму, которая выодит в консоль таблицу умножения "как на тетрадках"

def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1, 10):
            result = i * j
            print(f"{i} x {j} = {result:2d}", end="\t")
        print()

print_multiplication_table()
