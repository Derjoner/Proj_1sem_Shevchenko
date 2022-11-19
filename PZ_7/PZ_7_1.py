from random import randint

N = randint(1, 10)
S = input("Введите строку: ")
print("N:", N)

if len(S) > N:
    S = S[(len(S)-N):]
    print("Изменённая строка", S)
elif len(S) < N:
    S = (N-len(S))*'.' + S[:]
    print("Изменённая строка", S)