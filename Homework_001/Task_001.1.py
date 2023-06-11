# Написать программу, которая будет выводить в консоль ёлочку заданной высоты

def draw_tree(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    
height = int(input("Введите высоту ёлочки: "))
draw_tree(height)
