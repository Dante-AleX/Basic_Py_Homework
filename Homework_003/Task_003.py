# Создайте словарь со списком вещей для похода в качестве ключа 
# и их массой в качестве значения. Определите какие вещи влезут в 
# рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.

def pack_backpack(items, max_weight):
    possible_combinations = []
    current_combination = []

    def backtrack(weight, index):
        if weight > max_weight:
            return
        
        if weight == max_weight:
            possible_combinations.append(current_combination[:])
            return

        for i in range(index, len(items)):
            item, item_weight = items[i]
            if weight + item_weight <= max_weight:
                current_combination.append(item)
                backtrack(weight + item_weight, i + 1)
                current_combination.pop()

    backtrack(0, 0)
    return possible_combinations


# Пример использования функции
items = {
    'Спальник': 2,
    'Тент': 4,
    'Котелок': 1,
    'Фонарик': 0.5,
    'Палатка': 3,
    'Припасы': 2
}

max_weight = 7

possible_combinations = pack_backpack(list(items.items()), max_weight)

print("Возможные варианты комплектации рюкзака:")
for combination in possible_combinations:
    print(combination)
