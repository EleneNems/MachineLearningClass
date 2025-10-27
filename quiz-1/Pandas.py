import random

import pandas as pd
import numpy as np

# Create a Pandas Series from a Python list of numbers [10, 20, 30, 40, 50].
# Print its values, index, and describe its basic stats.
numbers = [10, 20, 30, 40, 50]
series = pd.Series(numbers)
print(series, '\n')
print(series.values, '\n')
print(series.index, '\n')
print(series.describe(), '\n')

# Create a DataFrame with the following data,
# Display the first and last rows using .head() and .tail().
dt1 = pd.DataFrame({
    'Name': ['Elene', 'Nika', 'Luka', 'Mari', 'Gio'],
    'Age': [21, 22, 20, 23, 19],
    'City': ['Tbilisi', 'Kutaisi', 'Tbilisi', 'Batumi', 'Tbilisi'],
    'Score': np.random.randint(0, 101, 5)
})


print(dt1.head(1), '\n')
print(dt1.tail(1), '\n')

# Add a new column called "Score" with random integers between 0–100.
score = np.random.randint(0, 101, 5)
dt1['Score'] = score
print(dt1)

# From your DataFrame, print only the "Name" column.
# Select only the rows where "Age" is greater than 20.
# Sort the DataFrame by "Score" in descending order
# Count how many people are from "Tbilisi".

print('\n', dt1['Name'])
morethan20 = dt1[dt1['Age'] > 20]
print('\n', morethan20)
sortedScore = dt1.sort_values(by='Score', ascending=False)
print('\n', sortedScore)
fromTbilisi = (dt1['City'] == 'Tbilisi').sum()
print('\n', fromTbilisi)

# Replace all scores below 50 with "Fail" and others with "Pass".
# Add a new column called "Passed" that is True if Score ≥ 50, else False.
# Remove the "City" column from the DataFrame.

# dt1['Score'] = np.where(dt1['Score'] < 50, 'Fail', 'Pass')
# print('\n', dt1)

dt1['Passed'] = dt1['Score'] > 50
print('\n', dt1)

dt1 = dt1.drop('City', axis=1)
print('\n', dt1)

# Create a new DataFrame of students with columns: "Name", "Subject", "Grade".
# Add at least 50 records with random grades (0–100), names and subjects.
# Find the average grade for each subject using .groupby().
# Find the highest grade and lowest grade overall.

names = ['Elene', 'Tako', 'Sopo', 'Mari', 'Anano', 'Maia', 'Nana', 'Nanuka', 'Nini', 'Shorena']
subjects = ['Science', 'Mathematics', 'History', 'Georgian', 'English', 'Art', 'Literature', 'Sport', 'Music']

nameCol = [random.choice(names) for _ in range(50)]
subjectCol = [random.choice(subjects) for _ in range(50)]

Students = pd.DataFrame({
    'Name': nameCol,
    'Subject': subjectCol,
    'Grade': np.random.randint(0, 101, 50)
})

avg = Students.groupby(['Subject']).mean(numeric_only=True)
print('\n', avg)
print('\n', min(Students['Grade']))
print('\n', max(Students['Grade']))

# Write the DataFrame to an Excel file (students.xlsx).
# Read that file back into a new DataFrame and print the first 3 rows.
# Append a new row (a new student) and write to a new Excel sheet called "Updated".

Students.to_excel('Students.xlsx', sheet_name="Students", index=False)

newStudents = pd.read_excel("Students.xlsx")
print(newStudents.head(3))

new_student = pd.DataFrame({
    'Name': ['Giorgi'],
    'Subject': ['Math'],
    'Grade': [88]
})

updatedStudents = pd.concat([newStudents, new_student], ignore_index=True)

with pd.ExcelWriter('Students.xlsx', engine='openpyxl', mode='a') as writer:
    updatedStudents.to_excel(writer, sheet_name='UpdatedStudents', index=False)

# Using the file_example_XLS_1000.xls or any Excel file: Find the average age.
# Find the most common (mode) country. Sort people alphabetically by first name.
# Write it in the next sheet in the file

exampleData = pd.read_excel('file_example_XLSX_1000.xlsx')
avg2 = exampleData['Age'].mean()
print('\n', avg2)

countryMode = exampleData['Country'].mode()
print('\n', countryMode)

sortedNames = exampleData.sort_values(by='First Name', ascending=True)

# with pd.ExcelWriter('file_example_XLSX_1000.xlsx', engine='openpyxl', mode='a') as writer:
#     sortedNames.to_excel(writer, sheet_name='SortedData', index=False)

# From your DataFrame, extract only rows where the name starts
# with “A” or “N” and save them into a new Excel file

newExcelData = sortedNames[sortedNames['First Name'].str.startswith(('A', 'N'))]
newExcelData.to_excel('filtered_file.xlsx', index=False)
