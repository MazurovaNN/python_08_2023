# 1. Напишите функцию для транспонирования матрицы

matrixZip = [[8, 9], [5, 6]] # создаю новую матрицу, используя вложенные списки.
zipped_rows = zip(*matrixZip) # передаю матрицу в zip с помощью оператора *. 
print(zipped_rows)

transpose_matrix = [list(row) for row in zipped_rows] # Вызываю каждую строку, а затем преобразую эту строку в новый список, который становится транспонированной матрицей.
print(transpose_matrix) # dspsdf. транспонированно. матрицe.

# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, 
# используйте его строковое представление.

# def flatten_dict(d):              # Вариант 1
#     new_dict = []
#     keyz = [i for i in d.keys()]
#     valuez = [i for i in d.values()]
#     i = 0
#     while len(new_dict) != len(keyz) + len(valuez):
#        new_dict.append(keyz[i])
#        new_dict.append(valuez[i])
#        i += 1
#     return new_dict

def flatten_dict(d):                # Вариант 2
    return [x for y in d.items() for x in y]

print(flatten_dict({'Alice':1, 'Bob':2}))

# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

op = int
count = 0
money = 0
count = 1
def withdraw(money):
    a = int(input('Введите сумму кратную 50 у.е.: '))
    if a % 50 == 0:
        if a < money:
            money = money - a - percent(a)
            print(f'Вы сняли {a}')
        else: print(f'Не хватает денег на счету')
    else: print('Сумма не кратна 50 у.е.')
    return money

def refil(money):
    b = int(input('Какую сумму вы хотите внести?: '))
    money = money + b
    print(money)
    return money

def percent(a):
    perc = a * 0.015
    print(perc)
    if perc > 30 and perc  < 300:
        return perc
    elif perc < 30:
        return 30
    else: return 300


while op != 4:
    op = int(input('Какую операцию хотите совершить?: \n 1. Снять деньги \n 2. Пополнить баланс \n 3. Узнать баланс\n 4.Выйти\n' ))
    if money > 5000000:
            money = money *0.9
    if count % 3 == 0:
        print('остаток от деления', count % 3 )
        money = money * 1.03
        print(f'Баланс: {money}')
    if op == 1:
        money = withdraw(money)
        print(f'Баланс: {money}')
    if op == 2:
        money = refil(money)
        print(f'Ваш Баланс: {money}')
    if op == 3:
        print(f'Ваш Баланс: {money}')
    count += 1

    







