a = 2
b = 300000
n = 1

while b > a:
    a = a * 1.1
    if a > b:
        n = n + 1
        break
    else:
        n = n + 1

print (n)
