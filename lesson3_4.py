a = 10
b = -2

def mf(a, b):
    c = 1
    for i in range(-b):
        c = c * a
        print(c)
    c = 1 / c
    return c

print(f'{mf(a, b):,.10f}'.replace(',', ' '))




# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.