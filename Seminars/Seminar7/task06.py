"""
Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

import os
import random
import string


def create_random_files(
    folder_path,
    extension,
    min_name_length=6,
    max_name_length=30,
    min_size=256,
    max_size=4096,
    num_files=42,
):
    if not extension.startswith("."):
        extension = f".{extension}"

    # Проверяем существование папки и создаем её, если она не существует
    os.makedirs(folder_path, exist_ok=True)

    for _ in range(num_files):
        while True:
            # Генерируем случайное имя файла
            name_length = random.randint(min_name_length, max_name_length)
            file_name = (
                "".join(
                    random.choice(string.ascii_letters + string.digits) for _ in range(name_length)
                )
                + extension
            )

            # Собираем полный путь к файлу
            file_path = os.path.join(folder_path, file_name)

            # Проверяем, существует ли файл с таким именем и расширением
            if not os.path.isfile(file_path):
                break

        # Генерируем случайное количество байт данных
        size = random.randint(min_size, max_size)
        data = os.urandom(size)

        # Создаем файл и записываем в него данные
        with open(file_path, "wb") as file:
            file.write(data)


def generate_files_with_extensions(extension_info, base_folder):
    for extension, num_files in extension_info.items():
        folder_path = os.path.join(base_folder, extension)
        create_random_files(folder_path, extension, num_files=num_files)


if __name__ == "__main__":
    base_folder = "./Seminars/Seminar7/task06"
    extension_info = {
        ".txt": 20,  # 20 файлов с расширением .txt
        ".jpg": 10,  # 10 файлов с расширением .jpg
        ".doc": 5,  # 5 файлов с расширением .doc
    }
    generate_files_with_extensions(extension_info, base_folder)
