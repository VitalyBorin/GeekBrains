print('Введите список, после каждого элемента нажимайте Enter. Для завершения ввода нажмите 111')
ml = []
while True:
    a = input()
    ml.append(a)
    if a == '111':
        break
print(ml)
ml1 = []
i = 0
print (len(ml))
while i <= len(ml) - 1:
    ml1.append(ml[i+1])
    ml1.append(ml[i])
    i += 2
    if (i + 2) > len(ml):
        break
    else:
        continue
print('ml', ml)
print('ml1', ml1)
