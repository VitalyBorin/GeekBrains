def mf (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print ('На ноль делить нельзя')

a1 = 0
a2 = 0

print ('Введите два числа. В ответ получите деление первого числа на второе')
a1 = int(input ('Введите первое число '))
a2 = int(input ('Введите второе число '))

print (mf (a1, a2))