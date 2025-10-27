import numpy as np
import random

# Create a 1D array of numbers from 5 to 25.
# Create a 2D array 3x4 filled with zeros.
# Create a 2D array 2x5 filled with ones.
arr1 = np.array(range(5, 26, 5))
arr2 = np.zeros((3, 4))
arr3 = np.ones((2, 5))

print(arr1, '\n', arr2, '\n', arr3)

# Generate a 1D array of 10 random integers between 0 and 50.
# Generate a 4x4 matrix of random floats between 0 and 1.
arr4 = np.random.randint(0, 51, size=10)
print(arr4)

arr5 = np.array(np.random.rand(4, 4))
print(arr5)

arr6 = np.array([3, 5, 2, 6, 1, 77, 7, 183, 51, 62]).reshape(2, 5)
print(arr6)

# Indexing and slicing Given an array of numbers from 1 to 20:
# Print the first 5 elements. Print the last 5 elements. Print every 3rd element.

arr7 = np.array(range(1, 21))
print(arr7[0:5])
print(arr7[-5:])
print(arr7[::3])

# Given a 4x4 matrix: extract the second row, last column, and the top-left 2x2 submatrix.

arr8 = np.random.randint(1, 100, size=16)
matrix = arr8.reshape(4, 4)
print(matrix)
print(matrix[1])
print(matrix[:, -1])
print(matrix[:2, :2])

# Create two 3x3 matrices of random integers (1-10). Calculate the sum of the matrices.
# Calculate element-wise multiplication. Calculate matrix multiplication.

arr9 = np.random.randint(1, 11, size=(3, 3))
arr10 = np.random.randint(1, 11, size=(3, 3))

sum_matrix = arr9 + arr10
print("\nSum of matrices:\n", sum_matrix)

element_mult = arr9 * arr10
print("\nElement-wise multiplication:\n", element_mult)

matrix_mult = np.dot(arr9, arr10)
print("\nMatrix multiplication:\n", matrix_mult)

# Create a 5x5 matrix with numbers 1-25 and reshape it.
# Find all even numbers in a 1D array and their indices.

arr11 = np.array(range(1, 26)).reshape(5,5)
print('\n', arr11)
flat = arr11.flatten()
evenindex = np.where(flat % 2 == 0)
evennums = flat[evenindex]
print("\nEven numbers:", evennums)
print("Their indixes:", evenindex[0])

# მოახდინეთ ორი მატრიცის შეკრების მოდელირება. მოიყვანეთ ორი მაგალითი
# (შემთხვევითი და სტატიკური რიცხვებისთვის)

A1 = [
    [1, 2],
    [3, 4]
]
B1 = [
    [5, 6],
    [7, 8]
]

A2 = np.random.randint(1, 21, (2, 2))
B2 = np.random.randint(1, 21, (2, 2))

print("The sum of two matrixes(ver1): ", np.array(A1) + np.array(B1))
print("The sum of two matrixes(ver2): ", np.array(A2) + np.array(B2))

# მოახდინეთ ორი მატრიცის გამრავლების მოდელირება. მოიყვანეთ ორი მაგალითი
# (შემთხვევითი და სტატიკური რიცხვებისთვის)

print("The product of two matrixes(ver1): ", np.array(A1) * np.array(B1))
print("The product of two matrixes(ver2): ", np.array(A2) * np.array(B2))

# შეავსეთ 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. წაშალეთ
# კლავიატურიდან შეტანილი რიცხვი. გამოიყენეთ numpy ბიბლიოთეკა.

A3 = np.random.randint(1, 11, (10, 10))
print(A3)
removeNum = int(input("enter the number you want to delete: "))
A3_new = A3[A3 != removeNum]
print(A3_new)

#ააგეთ ჭადრაკის დაფა. გამოიყენეთ numpy ბიბლიოთეკა.
board = np.zeros((8, 8), dtype=int)
board[1::2, ::2] = 1
board[::2, 1::2] = 1
print(board)