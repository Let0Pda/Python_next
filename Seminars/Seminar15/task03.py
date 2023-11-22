"""
Доработаем задачу 2.
Сохраняйте в лог файл раздельно: уровень логирования, дату события, имя функции (не декоратора),
аргументы вызова, результат.
"""
import json
from pathlib import Path
import logging


def my_json(func):
    file = Path(f"./Seminars/Seminar15/task02/{func.__name__}.json")
    if file.is_file():
        with open(file, "r", encoding="utf=8") as f1:
            b = json.load(f1)
    else:
        b = {}

    def wrapper(*args, **kwargs):
        res = kwargs
        res["arg"] = args
        res["result"] = func(*args, **kwargs)
        b.update(res)
        logging.info(f"{res}")
        return res

    return wrapper


@my_json
def my_func(num=1, *args, **kwargs):
    return num * 2


if __name__ == "__main__":
    my_log = "d:/GitTest/Python_next/Seminars/Seminar15/task03.log"
    logging.basicConfig(
        format="%(levelname)-8s %(asctime)s %(module)s %(funcName)s %(lineno)d %(message)s ",
        filename=my_log,
        encoding="utf8",
        level=logging.INFO,
        datefmt="%H:%M:%S %d-%m-%Y",
    )

    print(my_func(113, 656, num45=569))


# if __name__ == "__main__":
#     FORMAT = "{levelname:<8}, {asctime}, {name}, {msg}"
#     logging.basicConfig(
#         format=FORMAT, style="{", filename="mylog2.log", filemode="a", encoding="utf-8", level=logging.INFO
#     )
#     logger = logging.getLogger(__file__)
