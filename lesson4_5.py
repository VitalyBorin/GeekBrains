from functools import reduce

ml = [i for i in range(100,1000) if i % 2 == 0]
s = reduce((lambda x, y: x * y), ml)
print(s)