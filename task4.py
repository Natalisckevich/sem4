# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random as r
def form_funk (num, some_str):
    if num == 1:
        a = r.randint(0, 100)
        b = r.randint(0, 100)
        if a == 1 and b > 0:
            some_str += 'x+' + str (b)
        if a == 1 and b == 0:
            some_str += 'x' 
        if a == 0:
            some_str += str (b)
        if a > 1:
            some_str += str(a) + 'x+' + str (b)
        if a == 0 and b ==0:
            return some_str
        return some_str
    else:
        a = r.randint(0, 100)
        if a == 1:
            some_str += 'x' + '^' + str(num) + '+' + form_funk(num-1, some_str)
        if a == 0:
            some_str += form_funk(num-1, some_str)
        if a > 1:
            some_str += str(a) + 'x' + '^' + str(num) + '+' + form_funk(num-1, some_str)
        return some_str
        

some_str = ''
number = int(input('введите степень : '))
print(form_funk(number, some_str)+ ' = 0')