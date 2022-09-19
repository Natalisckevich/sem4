# Вычислить число π c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

number = float(input('Введите число с любым количеством знаков после запятой : '))
correctness = int(input('Задайте точность числа : '))
print(f'{round(number, correctness):.{correctness}f}')