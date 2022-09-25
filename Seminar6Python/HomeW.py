#Задача: предложить улучшения кода для уже решённых задач:
#С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

#Первоначальное решение

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def composition(number: int) -> list:
    list = []
    chislo = 1
    for i in range(1, number+1):
        chislo *= i
        list.append(chislo)
    return list
n = int(input('Введите число N: '))
print(f'Набор произведений от 1 до N:\n{composition(n)}')

#Решение с лямбдой

import math

n = int(input('Введите число N: '))
z = list(map(lambda x: math.factorial(x), range(1, n + 1)))
print(z)