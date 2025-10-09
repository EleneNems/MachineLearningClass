import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

a = [1, 7, 2]
myvar1 = pd.Series(a)
print(myvar1)

print(myvar.loc[0])

df = pd.read_csv("data.csv")
print(df.head(17))
print(df['Pulse'])

ex = pd.read_excel("Lecture_4.xlsx")
print(ex)

data = {
  "name" : ["elene", "mari", "tako"],
  "age" : [14, 62, 75]
}

df1 = pd.DataFrame(data)

df1.to_excel("output.xlsx")
