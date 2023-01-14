from random import randint

i = 0
N = randint(3, 10)
A = []
B = []
C = []

while i < N:
    A.append(str(randint(0, 50)))
    i += 1
else:
    i = 0

while i < N:
    B.append(str(randint(-50, -1)))
    i += 1

C = A + B
print(C.sort())

f1 = open('new_plus.txt', 'w')
for x in A:
    f1.writelines(x)
    f1.write(" ")
f1.close()
f1 = open('new_plus.txt')
print(f1.read())
f1.close()

f2 = open('new_minus.txt', 'w')
for x in B:
    f2.writelines(x)
    f2.write(" ")
f2.close()
f2 = open('new_minus.txt')
print(f2.read())
f2.close()

f3 = open('new_sort.txt', 'w')
f3.write("Элементы первого и второго файлов: ")
for i in open('new_plus.txt', encoding='UTF-8'):
    f3.write(i)
for i in open('new_minus.txt', encoding='UTF-8'):
    f3.write(i)
f3.write("\n")
f3.write("Элементы после сортировки: ")
f3.writelines()
