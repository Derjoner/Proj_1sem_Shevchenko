import numpy as np

A = np.random.randint(0, 20, (4, 4))

def gener(lis):
    yield from [n** 2 for n in lis]

C = list(gener(list(A[:, 1])))



print(C)
print(A, "\nfdf")