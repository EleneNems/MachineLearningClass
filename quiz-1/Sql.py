import mysql.connector
import random
import pandas as pd

mydb = mysql.connector.connect(
    host='localhost',
    password='',
    user='root',
    database='students'
)

mycursor = mydb.cursor()
command = "Insert into Students(Firstname, Lastname, GPA) Values(%s, %s, %s)"
val = ("Elene", 'Nemstsveridze', '4.00')
# mycursor.execute(command, val)
# mydb.commit()

# Write a query to select all columns from a table called students.
selectCom = "select * from Students"
mycursor.execute(selectCom)
data = mycursor.fetchall()
for row in data:
    print(row)

# Write random 20 columns in the table
names = ['Elene', 'Tako', 'Sopo', 'Mari', 'Anano', 'Maia', 'Nana', 'Nanuka', 'Nini', 'Shorena']
lastnames = ['Nemstsveridze', 'Qartvelishvili', 'Ujirauli', 'Tyebuchava', 'Joloxava', 'Beridze', 'Gogoladze', 'Kapanadze']

for _ in range(20):
    name = random.choice(names)
    lastname = random.choice(lastnames)
    GPA = round(random.uniform(0.1, 4.0), 2)

    insertCom = 'Insert into Students(Firstname, Lastname, GPA) Values(%s, %s, %s)'
    values = [name, lastname, GPA]
    mycursor.execute(insertCom, values)

# mydb.commit()


# Fetch only the students whose GPA is above 3.0.
# Fetch students whose last name starts with 'N' or 'Q'.
# Fetch students and order them by GPA descending.

selecting = ("select * from Students where GPA>3.0 AND (Firstname like 'N%' OR Firstname like 'Q%') order by GPA desc")
mycursor.execute(selecting)
filteredData = mycursor.fetchall()

for row in filteredData:
    id, firstname, lastname, gpa = row
    print(id, firstname, lastname, float(gpa))

df = pd.DataFrame(filteredData, columns=['ID', 'First Name', 'Last Name', 'GPA'])
df.to_excel('StudentsTable.xlsx', index=False)

updatingCom = "update Students set gpa=4.0 where Firstname='shorena'"
mycursor.execute(updatingCom)
mydb.commit()