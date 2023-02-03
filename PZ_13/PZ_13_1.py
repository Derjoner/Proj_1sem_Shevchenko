import numpy as np

B = []
A = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

B = A[-int((len(A)/2))::]

def gener(lis):
    for x in lis:
        yield

print(B)