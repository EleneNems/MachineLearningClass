# Ask the user to enter 5 names, store them in a list, and
# Print the list in alphabetical order.
# Remove any name that starts with “A”.

namelist = []
for i in range(5):
    num = input("Enter a name:")
    namelist.append(num)

print(sorted(namelist))
for name in namelist:
    if name.lower().startswith('a'):
        namelist.remove(name)
print(namelist)



# Given numbers = [1, 2, 3, 4, 5],
# create a new list that contains the squares of each number

numslist = [1, 2, 3, 4, 5]
newlist = []
for i in numslist:
    num = i ** 2
    newlist.append(num)

print(newlist)

# Create a tuple with 5 cities. Print the first and last city.
# Try to add a new city (see what happens).
# Convert the tuple to a list, add the city, and convert it back.

cities = ('Tbilisi', 'Kutaisi', 'Batumi', 'Poti', 'Zugdidi')
print(cities[0], cities[-1])
# cities.append('Rustavi')

cities_list = list(cities)
cities_list.append('Rustavi')
cities2 = tuple(cities_list)
print(cities2)

# Create two sets:  Add one new number to a and remove one from b.
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
a.add(6)
b.remove(6)
print(a, b)

# Create a dictionary for 3 students with keys: name, age, and grade.
# Print each student’s info.
# Add a new key called "passed" which is True if grade ≥ 60, else False.

Students = [
    {
        "name": 'Elene',
        "age": 20,
        "grade": 90
    },
    {
        "name": 'Nika',
        "age": 22,
        "grade": 50
    },
    {
        "name": 'Luka',
        "age": 21,
        "grade": 100
    }
]

print(Students)

for i in Students:
    i["passed"] = i["grade"] >= 60

print(Students)

# Ask the user for a fruit and quantity,
# Print the total price, or show an error if the fruit doesn’t exist.
prices = {"apple": 2, "banana": 1, "orange": 3}

fruit = input("enter the fruit you want: ")
quantity = int(input("enter how much you want: "))

if fruit in prices:
    total = prices[fruit] * quantity
    print(f"The total price for {quantity} {fruit}(s) is {total}")
else:
    print("Sorry, we don't have that fruit.")

#შეიყვანეთ ნებისმიერი რიცხი. იპოვეთ ამ რიცხვის ციფრთა რაოდენობა და დაბეჭდეთ.
realnum = int(input("Enter a number:"))
digits = len(str(abs(realnum)))
print("The digits are: ", digits)

# შეიყვანეთ ნებისმიერი რიცხი. დაადგინეთ არის თუ არა შეტანილი რიცხვი პალინდრომი.
# (მითითება: პალინდრომია რიცხვი, რომელიც მარჯვნიდან და მარცხნიდან ერთნაირად იკითხება). მაგ. 12521
palindrome = input("Enter a number: ")

if palindrome == palindrome[::-1]:
    print("The number is palindrome")
else:
    print("The number isn't a palindrome.")

# შეიყვანეთ სტრიქონი. დაითვალეთ რამდენჯერ შეგხვდათ სიმბოლო “a” დაბეჭდეთ შედეგი.

count=0
textstring = input("Enter a string: ")
print(textstring.count('a'))

