import re
import io

A = []
B = []
C = []
k = 0

f1 = open("text18-25.txt", encoding='UTF-8')
f2 = io.open("new_fa.txt", 'w', encoding='UTF-8')

for x in f1:
    A.append(re.split("\W+", x))
f1.close

f1 = open("text18-25.txt", encoding='UTF-8')

for x in f1:
    for y in x:
        for z in y:
            if z != "с":
                C.append(z)

f2.writelines(C)
f2.close

for x in A:
    for y in x:
        B.append(y)
        if y == "":
            B.remove('')

B = "".join(B)

for x in B:
    k += 1


print("Содержимое файла:\n" + open("text18-25.txt", encoding='UTF-8').read())
print("\nКоличество букв:", k)
f2 = io.open("new_fa.txt", encoding='UTF-8')
print("\nБез буквы 'с':\n"+ f2.read())
