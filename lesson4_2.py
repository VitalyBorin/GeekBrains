ml = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
ml1 = [j for i, j in zip(ml, ml[1:]) if j > i]

print(ml)
print(ml1)