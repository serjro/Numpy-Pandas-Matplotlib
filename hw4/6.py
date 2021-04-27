from itertools import cycle,count

for el in count(7):
    if el > 10:
        break
    else:
        print(el)


с = 0
for el in cycle("ABC"):
    if с > 5:
        break
    print(el)
    с += 1
