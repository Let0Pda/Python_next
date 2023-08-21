'''
Напишите программу, которая принимает две строки вида “a/b” — дробь с
числителем и знаменателем. Программа должна возвращать сумму и *произведение
дробей. Для проверки своего кода используйте модуль fractions.
'''
from fractions import Fraction


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def simplify_fraction(num, den):
    greatest_common_divisor = gcd(num, den)
    return num // greatest_common_divisor, den // greatest_common_divisor


def add_fractions(num1, den1, num2, den2):
    common_denominator = den1 * den2
    sum_num = num1 * den2 + num2 * den1
    return simplify_fraction(sum_num, common_denominator)


def multiply_fractions(num1, den1, num2, den2):
    return simplify_fraction(num1 * num2, den1 * den2)


def sum_and_product(f1, f2) -> None:
    num1, den1 = map(int, f1.split('/'))
    num2, den2 = map(int, f2.split('/'))

    sum_num, sum_den = add_fractions(num1, den1, num2, den2)
    product_num, product_den = multiply_fractions(num1, den1, num2, den2)

    print("Сумма дробей:", sum_num, "/", sum_den)
    print("Произведение дробей:", product_num, "/", product_den)


# Проверка
def sum_and_product_verification(f1, f2) -> None:
    frac1 = Fraction(f1)
    frac2 = Fraction(f2)
    sum_frac = frac1 + frac2
    product_frac = frac1 * frac2
    print("Проверка с помощью fractions:")
    print("Сумма дробей:", sum_frac)
    print("Произведение дробей:", product_frac)


f1 = input("Введите первую дробь в формате a/b: ")
f2 = input("Введите вторую дробь в формате a/b: ")


sum_and_product(f1, f2)
sum_and_product_verification(f1, f2)
