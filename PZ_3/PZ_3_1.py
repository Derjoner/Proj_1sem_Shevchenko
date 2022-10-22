# Ввод пользователем координат
x, y = input("Введите координаты X:"),  input("Введите координаты Y:")

while type(x) != int:
    try:
        x = int(x)
    except ValueError:
        print("Неправильно ввели!")
        x = input("Введите координаты X:")

while type(y) != int:
    try:
        y = int(y)
    except ValueError:
        print("Неправильно ввели!")
        y = input("Введите координаты Y:")

# Проверка истинности условия
if (x < 0) and (y > 0):
    print("Ваша точка лежит во второй четверти.")
else:
    print("Ваша точка не лежит во второй четверти.")
