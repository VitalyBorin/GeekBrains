a = int(input('Введите результат в первый день:'))
b = int(input('Введите целевой результат:'))
day = 1

while a < b:
    print(day, a)
    a = a*1.1
    day += 1

print (day)