# Дано целое число N (> 0). Если оно является степенью числа 3,
# то вывести TRUE, если не является - вывести FALSE.

n = input("Введите число: ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число: ")

while n > 3:
    n = n/3

if n == 3:
    print("True")
else:
    print("False")
