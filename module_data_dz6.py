GREAGORIAN = 1582 
year = int(input('Введите год в формате YYYY: ')) 
answer = "" 
if year <= GREAGORIAN: 
    answer = 'Неверный год' 
elif year % 4 != 0 or year % 100 == 0 and year % 400 !=0: 
    answer = 'Обычный' 
else: 
    answer = 'Високосный' 
print(answer) 