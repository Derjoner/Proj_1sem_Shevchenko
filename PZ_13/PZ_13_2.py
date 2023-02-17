# Вариант 25
# В матрице элементывторого столбца возвести в квадрат

import numpy as np

A = np.random.randint(0, 20, (4, 4))

print("Данная матрица:\n", A)

def gener(lis):
    yield from [n** 2 for n in lis]

C = list(gener(list(A[:, 1])))

A[:, 1] = C[:]

print("Полученная матрица:\n", A)
