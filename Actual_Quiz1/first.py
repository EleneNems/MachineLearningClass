import pandas as pd
import numpy as np
import random
import mysql.connector

# დაწერეთ პროგრამა, რომელიც შექმნის ლისტს 15 შემთხვევითი მთელი რიცხვით [10;100] შუალედიდან, შემდეგ დაბეჭდეთ
# ლისტში არსებული უმცირესი და უდიდესი რიცხვი, ხოლო ბოლოს წაშალეთ ყველა ელემენტი, რომელიც 7-ის ჯერადია და
# დაბეჭდეთ დარჩენილი ლისტი.
numList = np.random.randint(10, 101, 15)
print(numList)
print("Max:", max(numList))
print("Min:", min(numList))

index = np.where(numList % 7 == 0)
numList1 = np.delete(numList, index)
print(numList1)

# დაწერეთ პროგრამა, რომელიც ქმნის 6x6 Numpy მატრიცას შემთხვევითი მთელი რიცხვებით [1;50] შუალედიდან, გამოითვალეთ
# თითოეული რიგის საშუალო მნიშვნელობა და დაბეჭდეთ, შემდეგ შექმენით ახალი მატრიცა, რომელშიც თითოეული ელემენტი
# არის ორიგინალური ელემენტის კვადრატი და დაბეჭდეთ ახალი მატრიცა.
matrix = np.random.randint(1, 51, (6, 6))
print(matrix)
for row in matrix:
    print(sum(row))

newMatrix = matrix**2
print(newMatrix)

# დაწერეთ პროგრამა, რომელიც შექმნის DataFrame-ს 20 თანამშრომლით რომელსაც აქვს სვეტები: Name, Department, Salary,
# JoiningYear, ჩაწერეთ ეს მონაცემები Excel ფაილში employees.xlsx,

name = ['Elene', 'Tako', 'Mari', 'Sofi', 'Anano', 'Tiko', 'Ana']
departament = ['IT', 'Managers', 'Analysts', 'HR']
salary = np.random.randint(1500, 10000, 20)
joiningYear = np.random.randint(2000, 2026, 20)
nameCol = [random.choice(name) for _ in range(20)]
departamentCol = [random.choice(departament) for _ in range(20)]

df = pd.DataFrame(
    {
        'Name': nameCol,
        'Departament': departamentCol,
        'Salary': salary,
        'Joining Year': joiningYear
    }
)

df.to_excel('employees.xlsx', sheet_name='Data', index=False)

# შემდეგ წაიკითხეთ ფაილი Pandas-ის გამოყენებით,
# დაბეჭდეთ ყველა თანამშრომელი, რომლის მეტია 2500, დეპარტამენტი არის IT ან HR

data = pd.read_excel('employees.xlsx')
filteredData = data[(data['Salary'] > 2500) & ((data['Departament'] == 'HR') | (data['Departament'] == 'IT'))]
print(data)
print(filteredData)

# გამოთვალეთ საშუალო ხელფასი იმ
# თანამშრომელთათვის, რომლებიც კომპანიაში მუშაობენ 2018 წლიდან,

avr_sal = data[data['Joining Year'] >= 2018]['Salary'].mean()
print(avr_sal)

# შექმენით ახალი სვეტი AdjustedSalary, რომელიც ზრდის
# ხელფასს 10%-ით იმ თანამშრომელთათვის, რომელთა ხელფასი ნაკლებია 2000

data['AdjustedSalary'] = data['Salary'].where(data['Salary'] >= 2000, data['Salary'] + data['Salary'] * 10/100)
print(data)

# ბოლოს დაალაგეთ DataFrame ხელფასის
# მიხედვით კლებადი რიგით და დაბეჭდეთ პირველი 5 თანამშრომელი (ყველაზე მაღალი ხელფასი ვისაც აქვს).

sorted = data.sort_values(by='Salary', ascending=False)
print(sorted.head(5))

with pd.ExcelWriter('employees.xlsx', engine='openpyxl', mode='a') as writer:
    sorted.to_excel(writer, sheet_name='Sorted Data', index=False)

# sqlis nawili idk
db = mysql.connector.connect(
    host='localhost',
    user='root',
    database='machinelearningdb',
    password=''
)

mycursor = db.cursor()

insertCommand = "insert into employees(name, departament, salary, joiningYear) values(%s, %s, %s, %s)"
values = list(data[['Name', 'Departament', 'Salary', 'Joining Year']].itertuples(index=False, name=None))
mycursor.executemany(insertCommand, values)
db.commit()
