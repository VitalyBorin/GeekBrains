from math import factorial
def fact(n: int):
    for i in range(1, n + 1):
        yield factorial(i)

if __name__ == '__main__':
    count_f = input('Пожалуйста введите количество вычисленных факториалов: ')
    try:
        value = int(count_f)
    except ValueError as e:
        print(e)
        exit(1)
    for el in fact(value):
        print(el)
