s = []
def Sum(a, b):
    i = 0
    x = 0
    while i != b:
        s.append(a)
        a = a + 1
        i += 1
    return s

Sum(a = int(input("Введите первое число: ")), b = int(input("Введите второе число: ")))
print(sum(s))