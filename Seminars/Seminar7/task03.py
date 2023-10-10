"""
Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
    если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
    если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало.
"""


def func_sum(file1, file2, res):
    with (
        open(file1, "r", encoding="utf-8") as f1,
        open(file2, "r", encoding="utf-8") as f2,
        open(res, "w", encoding="utf-8") as res,
    ):
        digit = f1.readlines()
        name = f2.readlines()
        max_len = max(len(digit), len(name))
        min_len = min(len(digit), len(name))
        rate = max_len // min_len
        rate2 = max_len % min_len
        if len(digit) > len(name):
            name *= rate
            name += name[:rate2]
        else:
            digit *= rate
            digit += digit[:rate2]
        for i in range(max_len):
            a = eval(digit[i].replace("|", "*"))
            b = name[i].replace("\n", "")
            res.write(f"{b} = {a}\n")


if __name__ == "__main__":
    file1 = r"./Seminars/Seminar7/task01/task01.txt"
    file2 = r"./Seminars/Seminar7/task02/task02.txt"
    res = r"./Seminars/Seminar7/task03/task03.txt"
    func_sum(file1, file2, res)
