import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_excel("RealEstateData.xlsx")
print(df.head())
print(df.dtypes)

avg_price_city = df.groupby('city')['price'].mean()
print(avg_price_city)
print(df.groupby('city')['area'].mean())
print(df['rooms'].value_counts())

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='rooms', y='price', hue='city')
plt.title("Rooms vs Price by City")
plt.xlabel("Number of Rooms")
plt.ylabel("Price")
plt.show()

X = pd.get_dummies(df[['area', 'rooms', 'city']])
y = df['price']

print(X.head())
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
