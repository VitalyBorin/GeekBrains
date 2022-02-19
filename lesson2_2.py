ml = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
