from scipy.spatial.distance import cdist
import numpy as np
a = [[5, 3], [8, 2], [7, 8]]
b = [[0, 5], [3, 3], [2, 8]]
arr1 = cdist(a, b)

print(f'a = {a}')
print(f'b = {b}')
print("Value of cdist is :", arr1)


x = np.array([1, 3])
z = np.array([4, 5])
d = np.sqrt(np.sum((x-z)**2))
print(d)

min = arr1.min(axis=1)
min2 = arr1.min(axis=1).argsort()
print(f'min = {min}')
print(f'min2 = {min2}')

col = arr1.argmin(axis=1)[min2]
print(f'col = {col}')

col2 = arr1.argmin(axis=1)
print(f'col2 = {col2}')
