import numpy as np
import pandas as pd
import mysql.connector

name = ['Bread', 'Milk', 'Eggs', 'Juice', 'Ice-Cream']
cities = ['Tbilisi', 'Kutaisi', 'Khashuri', 'Gori']
nameCol = [np.random.choice(name) for _ in range(20)]
prices = np.random.randint(10, 501, 20)
quantities = np.random.randint(1, 21, 20)
citiesCol = [np.random.choice(cities) for _ in range(20)]
dates = np.random.randint(2023, 2026, 20)

products = pd.DataFrame(
    {
        'Name': nameCol,
        'City': citiesCol,
        'Price': prices,
        'Quantity': quantities,
        'Date': dates,
        'TotalSales': prices * quantities
    }
)

products['DiscountedPrice'] = products['Price'] - products['Price'] * 0.1
print(products)

products.to_excel("Products.xlsx", index=False)
productsRead = pd.read_excel("Products.xlsx")
print(productsRead)

avg = productsRead.groupby(by='City')['Price'].mean()
print(avg)

sortingTotalSales = productsRead.sort_values(by='TotalSales', ascending=False)
print(sortingTotalSales.head(1))

print(productsRead[(productsRead['TotalSales'] > 200) & (productsRead['City'] == 'Tbilisi')])

productsRead['Price'] = productsRead['Price'].where(productsRead['Price'] <= 400, 400)
print(productsRead)

revenuePerCity = productsRead.groupby(by='City')['TotalSales'].sum()
print(revenuePerCity)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    database='ml_db',
    password=''
)

myCursor = db.cursor()

InsertCommand = "insert into sale(name, city, price, quantity, saleDate, totalSale, discountedPrice) values(%s, %s, %s, %s, %s, %s, %s)"

# for _, row in productsRead.iterrows():
#     values = (row['Name'], row['City'], row['Price'], row['Quantity'], row['Date'], row['TotalSales'], row['DiscountedPrice'])
#     myCursor.execute(InsertCommand, values)
#
# db.commit()

SelectScript = "select * from sale where totalSale>3000"
myCursor.execute(SelectScript)
rows = myCursor.fetchall()

for row in rows:
    print(row)

data = pd.DataFrame(rows, columns=['ID', 'Name', 'City', 'Price', 'Quantity', 'Date', 'TotalSales', 'DiscountedPrice'])
sortedData = data.sort_values(by='TotalSales', ascending=False)

with pd.ExcelWriter("Sales.xlsx", engine="openpyxl", mode='a') as writer:
    sortedData.to_excel(writer, sheet_name="Sorted Sales Data New", index=False)
