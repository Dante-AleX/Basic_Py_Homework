# Напишите функцию, которая принимает на вход строку — 
# абсолютный путь до файла. Функция возвращает кортеж из трёх 
# элементов: путь, имя файла, расширение файла.

file_abs = r"D:\Documents\CV - Eng"

def path_name(file_path):
    full_file_name = file_path.split('\\')[-1]
    full_path = file_path.rsplit(full_file_name, 1)[0]
    
    if '.' in full_file_name:
        filename, exten_file = full_file_name.rsplit('.', 1)
    else:
        filename = full_file_name
        exten_file = ''
    
    return (full_path, filename, exten_file)

res_out = path_name(file_abs)
print(res_out)
