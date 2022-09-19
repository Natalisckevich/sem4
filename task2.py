# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input('Введите натуральное число : '))
res = str(number)+ '='
i=2
while i<=number:
    if is_prime(i) == True and number%i == 0:
        res += str(i) +'*'
        number /=i
    else: i += 1
print(res[:-1])