# Найти сумму чисел ряда 1, 2, 3, 4, ... от числа n до числа m.
# Суммирование оформить функцией с параметрами.
# Значения n и m программа должна запрашивать.

def Sum(a, b):
  i = 1
  sum = a
  while i+a <= b:
    sum = sum + (a+i)
    i += 1
  return sum

try:
  n = int(input("Введите первое число < второго: "))
  m = int(input("Введите второе число > первого: "))
  
  if n > m:
    print("Неправильно ввели! Первое число должно быть меньше второго.")
  else:
    print("Сумма числового ряда:", Sum(n, m))

except:
    print("Неправильно ввели данные!")
