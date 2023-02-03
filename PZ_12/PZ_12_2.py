# Вариант 25
# Составить генератор (yield), который выводит из строки только цифры.

from string import digits

i = 0
A = "A, f, 3, t, 5, j, 5, 2, F, A, 0"
B = []

def abc(srt):
  yield from [x for x in srt if x in digits]

print("Данная строка:", A, "\nИтог:", list(abc(A)))
