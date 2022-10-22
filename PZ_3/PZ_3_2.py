 # Ввод пользователем координат
x, y = input("Введите координаты X:"),  input("Введите координаты Y:")

# Обработка исключений
while type(x) != int:
    try:
        x = int(x)
    except ValueError:
        print("Неправильно ввели!")
        x = input("Введите координаты X:")

# Обработка исключений
while type(y) != int:
    try:
        y = int(y)
    except ValueError:
        print("Неправильно ввели!")
        y = input("Введите координаты Y:")


if (x%2 != 0) and (y%2 == 0) or (x%2 == 0) and (y%2 != 0):
    print("Данное поле является белым")
else:
    print("Данное поле не является белым")