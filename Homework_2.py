import numpy as np

#3
text1 = input("Enter a string:")
count_a = text1.count("a")
print(f'The letter "a" appears {count_a} times in the string.')

#5
text2 = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
count_s = text2.count("ს")
first_20 = text2[:20]
print("the first 20 symbols", first_20)
print(f"the letter 'ს' appears {count_s} times in the string.")

#11
text3 = "Have a nice day"
for i in range(len(text3) - 1, -1, -1):
    print(text3[i])

#13
name = input("Enter your name here: ")
lastname = input("Enter your last name here: ")

print(f"Your mail is: {name}.{lastname}@edu.ge")

#14
text4 = "This is a string. I am trying to write a long one, I am not that creative."
n = 5

for i in range(0, len(text4), n):
    print(text4[i:i+n])

#16
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

C = A + B
print(C)

A1 = np.random.randint(1, 51, (2, 3))
B1 = np.random.randint(1, 51, (2, 3))

C1 = A1 + B1
print(C1)

#18

C2 = A * B
print(f"The matrixes multipled are:\n", C2)

A2 = np.random.randint(1, 100, (3, 3))
B2 = np.random.randint(1, 100, (3, 3))

C3 = A2 * B2
print(f"The matrixes with randoms multipled are:\n", C3)
#20
A3 = np.random.randint(1, 11, (10, 10))
print("The original matrix\n", A3)
num_to_remove = int(input("Enter a number to remove: "))
A3_new = A3[A3 != num_to_remove]

print("\nMatrix after removing the number:\n", A3_new)

#23
board = np.zeros((8, 8), dtype=int)
board[1::2, ::2] = 1
board[::2, 1::2] = 1

print("Chessboard pattern:\n", board)
