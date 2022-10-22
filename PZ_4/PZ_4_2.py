# Ввод числа
n = input("Введите число: ")

# Обработчик исключений
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число: ")

# Нахождение степени 3
while n > 3:
  n = n/3

# Проверка числа на условие задачи
if n == 3:
  print("True")
else:
  print("False")