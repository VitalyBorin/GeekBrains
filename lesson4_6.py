from itertools import cycle, count

start_num = 4
for el in count(start_num):
    if el > 15:
        break
    else:
        print(el)

sp = ["A", "B", "C", "D"]
c = 0
for el in cycle(sp):
    if c > 100:
        break
    print(el)
    c += 1