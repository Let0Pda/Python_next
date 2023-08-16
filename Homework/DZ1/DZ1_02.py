# Напишите код, который запрашивает число и сообщает является ли оно простым
# или составным. Используйте правило для проверки: «Число является простым,
# если делится нацело только на единицу и на себя». Сделайте ограничение на
# ввод отрицательных чисел и чисел больше 100 тысяч.


num = int(input("Введите число: "))


def simple_and_compound(num):
    # check if 1-100000 and simple, compound
    if num < 1 or num > 100000:
        print("Число должно быть от 1 до 100000.")
    elif num == 1:
        print("Число не является ни простым, ни составным.")
    # construction
    else:
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        # final check
        if is_prime:
            print("Число является простым.")
        else:
            print("Число является составным.")
# start func


simple_and_compound(num)
