import json

def save_to_json(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Выполняем функцию и получаем результат
            result = func(*args, **kwargs)

            # Создаем словарь для сохранения параметров и результатов
            data = {
                'params': {
                    'args': args,
                    'kwargs': kwargs
                },
                'result': result
            }

            # Сохраняем данные в файл JSON
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)

            return result
        return wrapper
    return decorator

@save_to_json('result.json')
def multiply(a, b):
    return a * b

result = multiply(5, 7)
print(result)  # Выведет: 35
