import random

import mysql.connector
import numpy as np
import pandas as pd

#first
Students = [
    {
        'name': "Mari",
        'age': "20",
        'gpa': 3.2
    },
    {
        'name': "Tako",
        'age': "20",
        'gpa': 3.7
    },
    {
        'name': "Luka",
        'age': "22",
        'gpa': 2.0
    },
    {
        'name': "Anano",
        'age': "20",
        'gpa': 4.0
    },
]

gpaList=[]
for i in Students:
    gpaList.append(i['gpa'])

average = sum(gpaList)/len(gpaList)
print("Average: ", round(average, 2))
print("Highest: ", max(gpaList))
print("Standard deviation: ", np.std(gpaList))

studentsDt = pd.DataFrame(Students)
sortedStudents = studentsDt.sort_values(by='gpa', ascending=False)
sortedStudents.to_excel("StudentsData.xlsx", index=False)

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    database='students',
    password=''
)

cursor = mydb.cursor()
insertCommand = "insert into studentsdata(name, age, gpa) values(%s, %s, %s)"
values = np.array(pd.read_excel('StudentsData.xlsx'))

# for i in values:
#     cursor.execute(insertCommand, tuple(i))
#
# mydb.commit()

studentSelect = "select * from studentsdata where gpa>3.0"
cursor.execute(studentSelect)
filteredgpa = cursor.fetchall()
print(filteredgpa)


#second

sales = np.random.randint(100, 1001, 30)
discount = [round(random.uniform(0, 0.3), 2) for _ in range(30)]
day = ["10/27/20205" for _ in range(30)]

SalesData = pd.DataFrame(
    {
        'Day':day,
        'Sales':sales,
        'Discount': discount
    }
)
#
# SalesData.to_excel('SalesData.xlsx', index=False)
#
# insertCommandSales = "insert into salesdata(day, sales, discount) values(%s, %s, %s)"

# for index, row in SalesData.iterrows():
#     cursor.execute(insertCommandSales, (row['Day'], row['Sales'], row['Discount']))
# mydb.commit()

total = "SELECT COUNT(sales) FROM salesdata"
avg = "SELECT AVG(sales) FROM salesdata"

cursor.execute(total)
totalsales = cursor.fetchone()[0]  # use fetchone() and take the first item

cursor.execute(avg)
avgsales = cursor.fetchone()[0]    # same here

print("Total sales count:", totalsales)
print("Average sales:", round(avgsales, 2))

filteredsales = "select * from salesdata where sales>500 and discount < 0.1"
cursor.execute(filteredsales)
filteredsalesdata = pd.DataFrame(cursor.fetchall(), columns=['ID', 'Day', 'Sales', 'Discount'])


# with pd.ExcelWriter('SalesData.xlsx', engine='openpyxl', mode='a') as writer:
#     filteredsalesdata.to_excel(writer, sheet_name='Filtered Sales Data', index=False)

#third

someData = {
    'Elene': "Tbilisi",
    'Nika': "Kutaisi",
    'Luka': "Batumi"
}

df = pd.DataFrame(list(someData.items()), columns=['Name', 'Favourite City'])
df['VisitCount'] = np.random.randint(1, 11,  3)
print(df)

filteringVisits = df[df['VisitCount'] > 5]
print(filteringVisits)

# with pd.ExcelWriter('SalesData.xlsx', engine='openpyxl', mode='a') as writer:
#     filteringVisits.to_excel(writer, sheet_name='Cities Data', index=False)

insertCommandVisits = "insert into cities(Name, FavCountry, VisitCount) values(%s, %s, %s)"
for _, row in filteringVisits.iterrows():  # iterrows() gives (index, Series)
    cursor.execute(insertCommandVisits, (row['Name'], row['Favourite City'], row['VisitCount']))

mydb.commit()

