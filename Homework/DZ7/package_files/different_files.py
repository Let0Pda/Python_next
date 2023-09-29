"""
Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

import os
from creating_files import create_random_files


def generate_files_with_extensions(extension_info, base_folder):
    for extension, num_files in extension_info.items():
        folder_path = os.path.join(base_folder, extension)
        create_random_files(folder_path, extension, num_files=num_files)


if __name__ == "__main__":
    base_folder = "./Homework/DZ7/dz7_package"
    extension_info = {
        ".txt": 20,  # 20 файлов с расширением .txt
        ".jpg": 10,  # 10 файлов с расширением .jpg
        ".doc": 5,  # 5 файлов с расширением .doc
    }
    generate_files_with_extensions(extension_info, base_folder)
