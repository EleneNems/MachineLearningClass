import numpy as np
import pandas as pd
import mysql.connector
# Create a list of 20 random integers between 5 and 80.
# Print the list Print the sum, average, and count of even numbers
# Remove all numbers greater than 50 and print the updated list.

randlist = np.random.randint(5, 81, 20)
print(randlist)
print("Max:", max(randlist), '\nMin:', min(randlist), '\nAvg:', sum(randlist)/20)
indexes = np.where(randlist > 50)
randlist1 = np.delete(randlist, indexes)
print(randlist1)

# Create a dictionary of 5 students where: keys = student names values = their grades
# Tasks: Print all students with grades above 80 Add a new student Update one grade
# Delete the lowest grade student Print the average grade.

studentDic = {
    'Elene': 50,
    'Mari': 90,
    'Tako': 99,
    'Luka': 44,
    'Nika': 10
}

for name, grade in studentDic.items():
    if grade > 80:
        print(name)
    if name == 'Elene':
        studentDic[name] = 60

studentDic['new'] = 70
print(studentDic)

lowest_student = min(studentDic, key=studentDic.get)
del studentDic[lowest_student]
print(studentDic)

# Use collections.Counter to find: How many times each word appears The most common word.
from collections import Counter
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(words)
print(counter)
print(counter['apple'])     # 3  (how many times 'apple' appears)
print(counter.most_common())  # [('apple', 3), ('banana', 2), ('orange', 1)]
print(counter.most_common(1)) # [('apple', 3)]


# Generate a 6×6 NumPy array of random integers between 1 and 50.
# Print the matrix Print the mean of each row
# Create a new matrix that contains the square of every element Print both matrices.

matrix = np.random.randint(1, 51, (6, 6))
for row in matrix:
    print(row.mean())
matrix1 = matrix ** 2
print(matrix1)

# Create a 10×10 array of random integers between 1 and 100. Extract the first 3 rows and 4 columns
# Find the max, min, and average of the entire array Replace all even numbers with 0.

randnp = np.random.randint(1, 101, (10, 10))
print(randnp)
print(randnp[:3, :4])
print("Max:", randnp.max(), "\nMin:", randnp.min(), "\nAvg:", randnp.mean())
randnp[randnp % 2 == 0] = 0
print(randnp)

# Create a pandas DataFrame with 10 employees having: Name, Department, Salary, JoiningYear. Save to employees.xlsx Read it back
# Print employees with Salary > 3000 and department "IT" or "HR".
# Calculate the average salary of employees who joined after 2015.
# Add a column Bonus = 5% of salary for employees with Salary > 4000. Sort by salary (descending) and print top 3.

Name = ['Elene', 'Mari', 'Tako', 'Sofi', 'Anano', 'Lana', 'Ani', 'Anano']
Department = ['IT', 'HR', 'Business', 'Analysts', 'Math', 'Support']
Salary = np.random.randint(1000, 6000, 10)
JoiningYear = np.random.randint(2000, 2025, 10)
NameCol = [np.random.choice(Name) for _ in range(10)]
DepartmentCol = [np.random.choice(Department) for _ in range(10)]
dt = pd.DataFrame({
    'Name': NameCol,
    'Department': DepartmentCol,
    'Salary': Salary,
    'Joining Year': JoiningYear
})
dt.to_excel('Employees1.xlsx', index=False)
data = pd.read_excel('Employees1.xlsx')
print(data)

filtering = data[(data['Salary'] > 3000) & ((data['Department'] == 'IT')|(data['Department'] == 'HR'))]
print("filtered\n", filtering)

avg_sal = data[data['Joining Year'] > 2015]['Salary'].mean()
print(avg_sal)

data['Bonus'] = data['Salary'].where(data['Salary'] < 4000, data['Salary'] + data['Salary'] * 0.05)
print(data)

sorting = data.sort_values(by='Salary', ascending=False)
print(sorting.head(3))

# Create a table students(id, name, grade, year) Insert 3 rows from Python
# Select and print all rows where grade > 8 Update one grade Delete one student

db = mysql.connector.connect(
    host='localhost',
    user='root',
    database='ml_db',
    password=''
)

mycursor = db.cursor()

insertCommand = "INSERT INTO student (name, grade, year) VALUES (%s, %s, %s)"
values = [
    ('Elene', 10, 2005),
    ('Mari', 7, 2001),
    ('Tako', 6, 2004)
]

# mycursor.executemany(insertCommand, values)
# db.commit()

selecting = "select * from student where grade>8"
mycursor.execute(selecting)
selectedData = mycursor.fetchall()
print(selectedData)

updating = "update student set grade = 8 where name = 'Mari'"
mycursor.execute(updating)
db.commit()

deleting = "delete from student where name = 'Tako'"
# mycursor.execute(deleting)
# db.commit()


# Read data from a pandas DataFrame and insert it into a SQL table named products(name, price).
# Then use pandas.read_sql() to print all rows where price > 100.

NameProd = ['Bread', 'Milk', 'Egg', 'Juice']

products = pd.DataFrame(
    {
        'Name': NameProd,
        'Price': np.random.randint(0, 10, 4),
    }
)

print(products)

insertCommand11 = "insert into products(name, price) values(%s, %s)"
for _, row in products.iterrows():
    values = (row['Name'], row['Price'])
    mycursor.execute(insertCommand11, values)

db.commit()

productsDB = pd.read_sql("Select * from products", con=db)
print(productsDB)
