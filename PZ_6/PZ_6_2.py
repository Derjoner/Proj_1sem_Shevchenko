# Вариант 25
# Даны два списка A и B одинакого размера N.
# Сформировать новый список С того же размера,
# каждый элемент которого равен максимальному элементу из элементов списков А и В.

from random import randint

i = 0
N = randint(1, 10)
A = []
B = []
C = []

while i < N:
    A.append(randint(0, 100))
    i+=1
else:
  i = 0

while i < N:
    B.append(randint(0, 100))
    i+=1

for elem in A:
  if elem > B[A.index(elem)]:
    C.append(elem)
  else:
    C.append(B[A.index(elem)])

print("Исходные списки А и В:", A, B, "Список С:", C, sep="\n")
