import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

#mesame
age = np.random.randint(18, 70, 50)
income = np.random.randint(500, 5000, 50)

df = pd.DataFrame({
    "age": age,
    "income": income
})

print("Initial Data:\n", df.head())

plt.scatter(df["age"], df["income"])
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Scatter Plot: Age vs Income")
plt.show()


df["spending"] = np.random.randint(100, 2000, 50)

print("\nData With Spending Column:\n", df.head())

plt.scatter(df["age"], df["spending"])
plt.xlabel("Age")
plt.ylabel("Spending")
plt.title("Scatter Plot: Age vs Spending")
plt.show()


