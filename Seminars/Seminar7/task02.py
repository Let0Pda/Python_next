"""
Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
Полученные имена сохраните в файл.
"""
import random as rnd

# import string

# s = string.ascii_letters
# print(s)


def func_name(num, new_file):
    with open(new_file, "a", encoding="utf-8") as f:
        for _ in range(num):
            res = ""
            for _ in range(rnd.randint(4, 7 + 1)):
                a = chr(rnd.randint(1072, 1104))
                res += a
            glas = "аяуюоеёэиы"
            # res += glas[rnd.randint(0, len(glas) + 1)]
            res += rnd.choice(glas)
            f.write(f"{res.title()}\n")


if __name__ == "__main__":
    func_name(10, r"./Seminars/Seminar7/task02.txt")
