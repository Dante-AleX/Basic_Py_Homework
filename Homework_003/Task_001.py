# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.


# Генерируем список
import random

def list_gen(length, duplicate_probability):
    my_list = []
    for _ in range(length):
        if random.random() < duplicate_probability:
            # Генерируем случайное число и добавляем его дважды
            value = random.randint(1, 10)
            my_list.extend([value, value])
        else:
            # Генерируем случайное число и добавляем его в список
            value = random.randint(1, 10)
            my_list.append(value)
    return my_list

length = int(input("Введите желаемую длинну списка: "))  # Длинна списка
duplicate_probability = 0.2                            # Вероятность повтора символа 20%

my_list = list_gen(length, duplicate_probability)
print("Ваш список:", my_list)

# Печатаем данный список без повторяющихся символов
clean_list = list(set(my_list))
print("Ваш список без повторяющихся элементов: ", clean_list)
