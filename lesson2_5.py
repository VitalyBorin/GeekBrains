ml = [7, 5, 3, 3, 2]
print(ml)
b = 0
a = int(input())
for i in ml:
    if i <= a:
        ml.insert(b, a)
        break
    b += 1
print(ml)
