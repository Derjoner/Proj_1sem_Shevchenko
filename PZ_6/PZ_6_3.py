# Вариант 25 
# Даны множества A и B, состоящие соответственно из N1 и N2 точек (точки заданы своими координатами x, у). 
# Найти минимальное расстояние между точками этих множеств и сами точки, 
# расположенные на этом расстоянии (вначале выводится точка из множества A, затем точка из множества B).
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √(x2 – x1)2 + (у2 – y1)2.
# Для хранения данных о каждом наборе точек следует использовать по два списка:
# первый список для хранения абсцисс, второй — для хранения ординат.


from random import randint
from math import sqrt

i = 0
l = 0
N = randint(1, 5)
A = list({((1+elem)*randint(0, 25), (1+elem)*randint(0, 25)) for elem in range(N)})
X_A = []
Y_A = []
B = list({((1+elem)*randint(0, 25), (1+elem)*randint(0, 25)) for elem in range(N)})
X_B = []
Y_B = []
_R = []
_XY = []

def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num

def rasst(x1, x2, y1, y2):
    R = int_r(sqrt((x2-x1)**2+(y2-y1)**2))
    _R.append(R)
    _XY.append([(x1, y1), (x2, y2)])


for e in A:
  X_A.append(e[0])
for e in A:
  Y_A.append(e[1])

for e in B:
  X_B.append(e[0])
for e in B:
  Y_B.append(e[1])

while i < N:
  while l < N:
    rasst(X_A[i], X_B[l], Y_A[i], Y_B[l])
    l += 1
  i += 1
  l = 0

print("Множество А: \n", A)
print("Множество B: \n", B)
print("Все расстояния: \n", _R)
print("Минимальное растояние между точками:", min(_R))
print("Точки минимального расстояния(А и В):", *_XY[_R.index(min(_R))])
