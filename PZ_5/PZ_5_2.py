i = 0
def DigitCountSum(K, C=0, S=0):
    K = [int(x) for x in K]
    C = len(K)
    S = sum(K)
    print(f"Число: {''.join(map(str,K))}, Количество: {C}, Сумма: {S}")

while i <5:
    print(f"Число {i+1}:")
    DigitCountSum(K = list(input()))
    i+=1
else:
    print("Конец")