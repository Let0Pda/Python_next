'''
Напишите программу, которая принимает две строки вида “a/b” — дробь с
числителем и знаменателем. Программа должна возвращать сумму и *произведение
дробей. Для проверки своего кода используйте модуль fractions.
'''
from fractions import Fraction


def sum_and_product(f1, f2) -> None:
    frac1 = Fraction(f1)
    frac2 = Fraction(f2)
    sum_frac = frac1 + frac2
    product_frac = frac1 * frac2
    print("Сумма дробей:", sum_frac)
    print("Произведение дробей:", product_frac)


def sum_and_product_verification(f1, f2) -> None:
    frac1 = Fraction(f1)
    frac2 = Fraction(f2)
    sum_frac = frac1 + frac2
    product_frac = frac1 * frac2
    print("Сумма дробей:", sum_frac)
    print("Произведение дробей:", product_frac)


f1 = input("Введите первую дробь в формате a/b: ")
f2 = input("Введите вторую дробь в формате a/b: ")

sum_and_product(f1, f2)
sum_and_product_verification(f1, f2)
