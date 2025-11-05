import numpy as np
import pandas as pd
import mysql.connector

sales = np.random.randint(10, 500, 10)
print(sales)
for i in sales:
    if i > 200:
        print(i)

city = ['Tbilisi', 'Kutaisi', 'Gori', 'Khashuri']
cityCol = [np.random.choice(city) for _ in range(10)]
salesNew = pd.DataFrame({
    'Sales': sales,
    'DiscountedPrice': sales - sales * 0.05,
    'Cities': cityCol
})
print(salesNew)

avg = salesNew.groupby('Cities')['Sales'].mean()
print(avg)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    database='ml_db',
    password=''
)

myCursor = db.cursor()

insertCommand = 'Insert into sales(sales, discountedPrice, cities) values(%s, %s, %s)'

for _, row in salesNew.iterrows():
    values = row['Sales'], row['DiscountedPrice'], row['Cities']
#     myCursor.execute(insertCommand, values)
#
# db.commit()

sortedData = salesNew.sort_values(by='Sales', ascending=False)
print(sortedData.head(5))

salesNew.to_excel('Sales.xlsx', index=False)

with pd.ExcelWriter('Sales.xlsx', engine='openpyxl', mode='a') as writer:
    sortedData.to_excel(writer, sheet_name='Sorted Sales Data', index=False)