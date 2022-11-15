# Вариант 25
# Дан целочисленный список размера N.
# Проверить, чередуются ли в нём чётные и нечётные числа.
# Если чередуются, то вывести 0, если нет, то вывести порядковый номер первого элемента,
# нарущающего закономерность.

from random import randint

i = 0
N = randint(1, 10)
A = []

while i < N:
    A.append(randint(0, 100))
    i += 1

print("Данный список:", A)

for x in A:
    if A.index(x) == N-1:
        y = A[A.index(x) - 1]
    else:
        y = A[A.index(x) + 1]
    if (x % 2 == 0) and (y % 2 == 0):
        print("Порядковый номер числа:", A.index(y) + 1)
        break
    elif (x % 2 != 0) and (y % 2 != 0):
        print("Порядковый номер числа:", A.index(y) + 1)
        break
else:
    print(0)
