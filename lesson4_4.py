ml = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
ml1 = []

for i in ml:
    n = 0
    for j in ml:
        if i == j:
            n += 1
    if n < 2:
        ml1.append(i)