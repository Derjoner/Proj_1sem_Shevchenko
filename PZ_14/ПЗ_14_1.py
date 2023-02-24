# Вариант 25
# В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
# Посчитать количество полученных элементов.

import re

p = re.compile(r"«[А-ЯЁ].*?»")
f1 = open("Dostoevsky.txt", encoding="UTF-8")
s = f1.read()
f1.close()
li = set(p.findall(s))
print("Все произведения писателя:", *li, "\nОбщие количество:", len(li))