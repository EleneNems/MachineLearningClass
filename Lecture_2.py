import numpy as np
from numpy import random

x = random.randint(100, size=(5))
print(x)

print("_________________________________________________________")

ar = np.array(40)
print(ar)

ar2 = np.array([4, 5, 6, 8])
print(ar2)

ar3 = np.array([[4, 5, 6, 18],
                [4, 15, 6, 49],
                [7, 8, 11, 19],
                ])

ls = [
[4, 5, 6, 8],
[4, 15, 8],
[4, 5, 6, 8],
]

print(ls[1][1])
print(ar3)
print(ls)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:])

print("_________________________________________________________")

arr1 = np.array([1, 2, 3, 4, 5])
x = arr1.copy()
arr1[0] = 42
arr1[1] = 36

print(arr1)
print(x)

print("_________________________________________________________")

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr2.reshape(2, 2, 3)
print(newarr)




