# Даны два целых числа A и B (A < B).
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B),
# а также количество N этих чисел.

a = int(input("Введите первое число < второго: "))
b = int(input("Введите второе число > первого: "))
x = 0
i = a

try:
    while a > b:
        print("Неправильно ввели! Первое число должно быть меньше второго.")
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))

    while i != b+1:
        print(i)
        i += 1
        x += 1
    else:
        print("Количество чисел: ", x)
except:
    print("Неправильно ввели данные!")
