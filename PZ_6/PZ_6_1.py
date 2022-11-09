from random import randint
i = 0
Ds = []
a = randint(1, 10)
while i < a:
    Ds.append(randint(0, 100))
    i+=1

for x in Ds:
    if Ds.index(x) == a-1:
        y = Ds[Ds.index(x) - 1]
    else:
        y = Ds[Ds.index(x) + 1]
    if (x % 2 == 0) and (y % 2 ==0):
        print(y)
        break
    elif (x % 2 == 0) and (y % 2 ==0):
        print(y)
        break
