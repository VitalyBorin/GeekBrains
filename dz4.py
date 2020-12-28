n=str(input('Введите многозначное целове положительное число:'))
max = 0
i = 0

while i < len(n):
    if int(n[i]) > max:
        max = int(n[i])
    i += 1
print('Наибольшая цифра в числе:', max)
