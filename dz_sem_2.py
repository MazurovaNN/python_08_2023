# 1. Решить задачи, которые не успели решить
# на семинаре.
# В отдельной папке

# 2. Напишите программу, которая получает целое 
# число и возвращает его шестнадцатеричное 
# строковое представление. Функцию hex 
# используйте для проверки своего результата.

def to_hex(num):
    hex_digits = "0123456789abcdef"
    hex_str = ""
    while num > 0:
        hex_str = hex_digits[num % 16] + hex_str
        num = num // 16
    return hex_str

# Пример применения функции
a: int = int(input('Введите значение '))
num = a
hex_str = to_hex(num)
print(f"Шестнадцатеричное представление числа {num} - {hex_str}")

# 3. Напишите программу, которая принимает две строки вида 
#“a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.  

def process_fractions(frac1_str, frac2_str):
    # Преобразую дроби из строк в числа
    num1, denom1 = map(int, frac1_str.split("/"))
    num2, denom2 = map(int, frac2_str.split("/"))

    # Вычисляю сумму дробей
    sum_frac_num = num1 * denom2 + num2 * denom1
    sum_frac_denom = denom1 * denom2
    sum_frac = (sum_frac_num, sum_frac_denom)

    # Вычисляю произведение дробей
    prod_frac_num = num1 * num2
    prod_frac_denom = denom1 * denom2
    prod_frac = (prod_frac_num, prod_frac_denom)

    return sum_frac, prod_frac

# Пример применения функции
frac1_str = "7/9"
frac2_str = "5/6"

sum_frac, prod_frac = process_fractions(frac1_str, frac2_str)

print(f"Сумма дробей {frac1_str} и {frac2_str} - {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей {frac1_str} и {frac2_str} - {prod_frac[0]}/{prod_frac[1]}")
