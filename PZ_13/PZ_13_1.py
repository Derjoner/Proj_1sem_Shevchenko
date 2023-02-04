import numpy as np

A = np.random.randint(0, 20, (4, 4))

def gener(lis):
    yield from [item for subl in lis for item in subl]


C = list(gener(A[-int((len(A)/2))::]))



print("Данная матрица: \n", A, '\nСумма второй половины матрицы: ',  sum(C))