# Вариант 25
# Средствами языка Python сформировать два текстовых файла (.txt), 
# содержащих по одной последовательности из целых положительных и отрицательных чисел. 
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Элементы после сортировки:
# Количество элементов:
# Минимальный элемент кратный 2:
# Максимальный элемент кратный 5:

from random import randint

i = 0
N = randint(3, 10)
A = []
B = []
C = []
D = []
_min = []
_max = []


# Наполнение списка A и С
while i < N:
    q = randint(0, 50)
    A.append(str(q))
    C.append((q))
    i += 1
else:
    i = 0

# Наполнение списка B и С
while i < N:
    q = randint(-50, -1)
    B.append(str(q))
    C.append((q))
    i += 1

# Действия для решения остальных критериев

# Сортировка
C.sort()

# Преобразование в строку и подсчёт количества
for w in C:
    C[C.index(w)] = str(w)
    D.append(w)

# Выявление минимального и кратного 2
for j in D:
    if (j % 2) == 0:
        _min.append(j)

# Выявление максимаьного и кратного 5
for j in D:
    if (j % 5) == 0:
        _max.append(j)


# Основная работа с файлами
f1, f2 = open('new_plus.txt', 'w'), open('new_minus.txt', 'w')
for x in A:
    f1.writelines(x)
    f1.write(" ")
for x in B:
    f2.writelines(x)
    f2.write(" ")
f1.close()
f2.close()


f3 = open('new_sort.txt', 'w')
f3.write("Элементы первого и второго файлов: ")
for i in open('new_plus.txt', encoding='UTF-8'):
    f3.write(i)
for i in open('new_minus.txt', encoding='UTF-8'):
    f3.write(i)
f3.write("\n")
f3.write("Элементы после сортировки: ")
for i in C:
    f3.write(i)
    f3.write(" ")
f3.write("\n")
f3.write("Количество элементов: ")
f3.write(str(len(D)))
f3.write("\n")
f3.write("Минимальный элемент кратный 2: " + str(min(_min)))
f3.write("\n")
f3.write("Максимальный элемент кратный 5: " + str(max(_max)))
f3.close()

# Вывод
f1, f2, f3 = open('new_plus.txt'), open('new_minus.txt'), open('new_sort.txt')
print("Файл положительных чисел: " + f1.read() + "\nФайл отрицательных чисел: " + f2.read() + "\nОбработаный файл:\n" + f3.read())
