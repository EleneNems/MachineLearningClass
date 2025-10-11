import pandas as pd
import numpy as np
import random
import string

#1
col1 = [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for i in range(100)]
col2 = np.random.randint(0, 11, 100)
col3 = np.random.randint(1, 8, 100)
col4 = np.random.permutation(np.arange(1, 101))

df = pd.DataFrame({
    'RandomString': col1,
    'RandomInt[0,10]': col2,
    'RandomInt[1,7]': col3,
    'RandomUniqueInt[1,100]': col4
})

#2
names = ['Elene', 'Tako', 'Sopo', 'Mari', 'Anano', 'Maia', 'Nana', 'Nanuka', 'Nini', 'Shorena']
lastname = ['Nemstsveridze', 'Qartvelishvili', 'Ujirauli', 'Tyebuchava', 'Joloxava']
col11 = np.random.randint(1, 101, 50)
col22 = [random.choice(names) for _ in range(50)]
col33 = [random.choice(lastname) for _ in range(50)]
col44 = np.random.randint(2000, 5001, 50)

df2 = pd.DataFrame({
    'RandomInt[1,100]': col11,
    'RandomName': col22,
    'RandomLastName': col33,
    'RandomInt[2000, 5001]': col44
})

with pd.ExcelWriter('data.xlsx', 'openpyxl') as writer:
    df.to_excel(writer, sheet_name='SheetOne', index=False)
    df2.to_excel(writer, sheet_name='SheetTwo', index=False)

#3
data = pd.read_excel('data.xlsx', sheet_name=None)

with pd.ExcelWriter('datanew.xlsx', engine='openpyxl') as writer:
    for sheet_name, df in data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)


#4
data2 = pd.read_excel('data.xlsx', sheet_name='SheetOne')
filtering = data2[data2['RandomString'].str.contains('a')]

with pd.ExcelWriter('datanew.xlsx', engine='openpyxl', mode='a') as writer:
    filtering.to_excel(writer, sheet_name='SheetThree', index=False)

#5
data3 = pd.read_excel('data.xlsx', sheet_name='SheetTwo')
filtering2 = data3[data3['RandomInt[2000, 5001]'] > 4000]

with pd.ExcelWriter('datanew.xlsx', 'openpyxl', mode='a') as writer:
    filtering2.to_excel(writer, sheet_name='SheetFour', index=False)

#6
data4 = pd.read_excel('file_example_XLSX_1000.xlsx')
data4_sort = data4.sort_values(by='Id')
print(data4_sort)

average = data4['Age'].mean()
print('The average for ages are:', average)

mode = data4['Age'].mode()[0]
print("The mode is: ", mode)

median = data4['Age'].median()
print("The median is: ", median)

youngestid = data4['Age'].idxmin()
oldestid = data4['Age'].idxmax()

youngest = data4.loc[youngestid]
oldest = data4.loc[oldestid]
print('The oldest is: ', oldest)
print('The youngest is: ', youngest)

#7
data5 = pd.read_excel('staff_1000.xlsx')
filtering3 = data5[(data5['Age'] >= 30) & (data5['Age'] <= 40)]

with pd.ExcelWriter("staff_age.xlsx", engine="openpyxl") as writer:
    filtering3.to_excel(writer, index=False)
