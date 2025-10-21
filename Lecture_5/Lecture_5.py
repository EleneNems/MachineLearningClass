import mysql.connector
import random
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ml_db"
)

mycursor = mydb.cursor()
# print(mydb)
# print(mycursor)

sql = "insert into students (Name, Lastname) Values (%s, %s)"
val = ("Elene", "Nemstsveridze")
mycursor.execute(sql, val)
mydb.commit()

#write 50 random columns, name, lastname
names = ['Elene', 'Tako', 'Sopo', 'Mari', 'Anano', 'Maia', 'Nana', 'Nanuka', 'Nini', 'Shorena']
lastnames = ['Nemstsveridze', 'Qartvelishvili', 'Ujirauli', 'Tyebuchava', 'Joloxava', 'Beridze', 'Gogoladze', 'Kapanadze']

sql = "INSERT INTO students (Name, Lastname) VALUES (%s, %s)"
val = []
for i in range(50):
  first=random.choice(names)
  last = random.choice(lastnames)
  val.append((first, last))

# mycursor.executemany(sql, val)
# mydb.commit()

print(f"{mycursor.rowcount} records inserted successfully!")

# read students table data and write only those students whose lastname starts with N Q or U in name.xlsx file,
# count how many are there and write the data name ascending.
query = "select * from students where Lastname like 'N%' Or Lastname like 'Q%' Or  Lastname like 'U%' order by Name asc"

data = pd.read_sql(query, mydb)
print(data)

count = len(data)
print(f"There are {count} students whose last name starts with N, Q, or U.")

# data.to_excel("name.xlsx", sheet_name="Filtered_Students", index=False)
# print("Data written successfully to name.xlsx.")