def my_func(a, b, c):
    ml = [a, b, c]
    ml.remove(min(ml))
    return sum(ml)

a = 60009
b = 2000
c = 30099

print(my_func(a, b, c))

# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.