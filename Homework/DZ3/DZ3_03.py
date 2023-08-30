'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой
в качестве значения. Определите какие вещи влезут в рюкзак передав его
максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.

*Верните все возможные варианты комплектации рюкзака.
'''


def backpack(items, max_weight):
    """
    Рекурсивно находит все возможные комбинации предметов для рюкзака.

    Args:
        items (list): Список предметов, каждый элемент - кортеж (предмет, вес).
        max_weight (float): Максимальный допустимый вес рюкзака.

    Returns:
        list: Список списков, представляющих возможные комбинации предметов.
    """
    if not items or max_weight == 0:
        return [[]]

    item, weight = items[0]
    rest_items = items[1:]

    # Получаем комбинации без текущего предмета
    combinations_without_item = backpack(rest_items, max_weight)

    combinations_with_item = []
    if weight <= max_weight:
        # Получаем комбинации с текущим предметом
        combinations_with_item = backpack(
            rest_items, max_weight - weight)
        for combination in combinations_with_item:
            combination.append(item)

    return combinations_without_item + combinations_with_item


def stuffing():
    """
    Основная функция для запуска программы подбора предметов в рюкзак.
    """
    items = {
        'Спальник': 4,
        'Палатка': 7,
        'Вода': 2,
        'Еда': 5,
        'Одежда': 3,
        'Топор': 2,
        'Фонарь': 0.5,
        'Компас': 0.2,
        'Посуда': 0.6
    }

    max_weight = float(
        input("Введите максимальную грузоподъемность рюкзака: "))

    selected_combinations = backpack(list(items.items()), max_weight)
    selected_combinations = selected_combinations[1:]

    if not selected_combinations:
        print("Нет подходящих комбинаций.")
    else:
        print("Возможные варианты комплектации рюкзака:")
        for i, combination in enumerate(selected_combinations, start=1):
            total_weight = sum(items[item] for item in combination)
            print(f"{i}. {combination} (Вес рюкзака: {total_weight})")


# Запускаем основную часть программы
stuffing()
