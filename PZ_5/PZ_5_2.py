i = 1

def DigitCountSum(K, C, S):
  while(K):
    C = C + 1
    S = S + K % 10
    K = K // 10
  print('Цифр:', C)
  print('Сумма:', S)

try:
  while i <= 5:
    a = int(input(f"Введите {i} число: "))
    DigitCountSum(a, C = 0, S = 0)
    i += 1
except:
  print("Неправильно ввели!")
