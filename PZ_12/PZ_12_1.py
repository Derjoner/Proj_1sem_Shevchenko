# Вариант 25
#  Дана последовательность целых чисел.
# Поменять местами её первую и последнюю трети.

from random import randint

i = 0
A = []
B = []
C = []

while i < 9:
  A.append(randint(1, 25))
  i += 1

def gener(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]

B = list(gener(A, 3))

B[0], B[-1] = B[-1], B[0]

for x in B:
  for y in x:
    C.append(y)
    
print("Данный список: ", A, "\nПеределанный список: ", C)
