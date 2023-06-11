# Треугольник существует только тогда, когда сумма любых двух его 
# сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, 
# равнобедренным или равносторонним.


def triangle_check(a, b, c):
    if a+b<=c or a+c<=b or b+c<=a:
        print('Такого треугольника быть не может!')
    else:
        if a==b or a==c or b==c:
            print('Данный треугольник Равнобедренный')
        elif a==b==c:
            print('Данный треугольник Равносторонний')
        else:
            print('Данный треугольник Разносторонний')

a = int(input('Введите первую сторону треугольника: '))
b = int(input('Введите вторую сторону треугольника: '))
c = int(input('Введите третью сторону треугольника: '))

triangle_check(a, b, c)
