# Напишите функцию принимающую на вход только ключевые 
# параметры и возвращающую словарь, где ключ — значение 
# переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def create_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        if not isinstance(key, (int, float, str, bool)):
            key = str(key)
        result_dict[value] = key
    return result_dict

result = create_dict(a=42, b='hello', c=True, d=3.14)
print(result)
