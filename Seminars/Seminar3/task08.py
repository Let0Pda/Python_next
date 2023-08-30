'''
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а
значение — кортеж вещей. Ответьте на вопросы:
Какие вещи взяли все три друга
Какие вещи уникальны, есть только у одного друга
Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь
отсутствует
Для решения используйте операции с множествами. Код должен расширяться на
любое большее количество друзей.
'''


def main() -> None:
    friends_items = {
        "Вася": ("рюкзак", "палатка", "спальник", "фонарик"),
        "Петя": ("рюкзак", "спальник", "еда", "топор"),
        "Игорь": ("рюкзак", "палатка", "фонарик", "одеяло")
    }

    # Какие вещи взяли все
    common_items = set.intersection(*map(set, friends_items.values()))
    common = ', '.join(common_items)
    print("\nВещи, которые взяли все три друга: \n" + common.title())

    # Есть только у одного друга
    all_items = set.union(*map(set, friends_items.values()))
    unique_items = {item: friend for item in all_items for friend,
                    friend_items in friends_items.items() if item in
                    friend_items and sum(item in items for items in
                                         friends_items.values()) == 1}
    print("Уникальные вещи, которые есть только у одного друга:")
    for item, friend in unique_items.items():
        print(f"'{item.title()}' есть только у {friend}")

    # Есть у всех кроме одного
    print("Вещи, которые есть у всех кроме одного друга:")
    for item in all_items:
        friends_with_item = [
            friend for friend, friend_items in friends_items.items() if item
            in friend_items]
        if len(friends_with_item) == len(friends_items) - 1:
            missing_friend = next(
                friend
                for friend in friends_items
                if friend not in friends_with_item
            )
            print(f"'{item.title()}' есть у всех, кроме {missing_friend}")


main()
