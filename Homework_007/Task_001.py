# Напишите функцию группового переименования файлов. Она должна:
# 1) принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# 2) принимать параметр количество цифр в порядковом номере.
# 3) принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# 4) принимать параметр расширение конечного файла.
# 5) принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 
# Соберите из созданных  функций пакет для работы с файлами.


import os
from random import sample
from string import ascii_letters


def rename_files(end_name, digits, source_extension, dest_extension, name_range=(0, -1)):
    files = os.listdir(os.path.join(os.getcwd(), PACK_NAME_WITH_EXAMPLES))

    filtered_files = [f for f in files if f.endswith(source_extension)]

    for i, file in enumerate(filtered_files, 1):
        old_name = os.path.splitext(file)[0][name_range[0]:name_range[1]]

        new_name = f"{old_name}_{end_name}_{str(i).zfill(digits)}{dest_extension}"

        old_path = os.path.join(os.getcwd(), PACK_NAME_WITH_EXAMPLES, file)
        new_path = os.path.join(os.getcwd(), PACK_NAME_WITH_EXAMPLES, new_name)
        os.rename(old_path, new_path)


def creating_demo_folder(number_files: int, extension: str):
    os.mkdir(PACK_NAME_WITH_EXAMPLES)

    for _ in range(number_files):
        file_name = ''.join(sample(ascii_letters, 5)) + extension
        demo_path = os.path.join(os.getcwd(), PACK_NAME_WITH_EXAMPLES, file_name)

        with open(demo_path, 'w'):
            continue


global PACK_NAME_WITH_EXAMPLES
PACK_NAME_WITH_EXAMPLES = 'new_folder'

# запускаем 1 раз, при запуске 2 раза закомментировать строчку 51
creating_demo_folder(10, '.txt')

rename_files('new_', 2, '.txt', '.jpg', (0, 3))