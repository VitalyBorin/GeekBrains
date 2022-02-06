n = int(input('please enter number'))
m = 0
i = 0
while n > 0:
    if (n % 10) > m:
        m = n % 10
    n = n // 10
print (m)