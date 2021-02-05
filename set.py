import numpy as np
D = np.array([[2, 3, 1], [11, 9, 5], [4, 8, 6], [2, 3, 5]])
print(D.shape[0])
print(D.shape)

x = set(range(0, D.shape[0]))
print(f'x = {x}')
s = set(range(0, D.shape[0])).difference([3])
print(f's = {s}')
