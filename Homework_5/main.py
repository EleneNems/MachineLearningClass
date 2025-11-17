import pandas as pd
import random

num_students = random.randint(50, 100)
names = ["Elene", "Tako", "Nika", "Giorgi", "Sandro", "Mari", "Luka", "Ana", "Dato", "Nino"]
genders = ["Male", "Female"]
subjects = ["Math", "Python", "Physics", "Biology", "AI", "Chemistry"]

students = {
    "name": [random.choice(names) for _ in range(num_students)],
    "age": [random.randint(18, 30) for _ in range(num_students)],
    "gender": [random.choice(genders) for _ in range(num_students)],
    "hours_studied": [random.randint(0, 50) for _ in range(num_students)],
    "subject": [random.choice(subjects) for _ in range(num_students)],
}

students["passed"] = [
    "Yes" if h > random.randint(10, 25) else "No"
    for h in students["hours_studied"]
]

students_df = pd.DataFrame(students)
print(students_df.head())
print("Total students:", len(students_df))

print("Average age:", students_df["age"].mean())

print("\nGender distribution:")
print(students_df["gender"].value_counts())

pass_rate = (students_df["passed"].value_counts().get("Yes", 0) / len(students_df)) * 100
print("\nPass percentage:", round(pass_rate, 2), "%")

print("\nAverage hours studied per subject:")
print(students_df.groupby("subject")["hours_studied"].mean())

print("\nStudents who studied over 40 hours:")
print(students_df[students_df["hours_studied"] > 40])

#namdvili monacemebi
df1 = pd.read_csv("Student_performance_data _.csv")

studentsReal = pd.DataFrame({
    "name": df1["StudentID"],
    "age": df1["Age"],
    "gender": df1["Gender"],
    "hours_studied": df1["StudyTimeWeekly"],
    "subject": df1["GradeClass"],
    "passed": df1["GPA"].apply(lambda x: "Yes" if x >= 2.5 else "No")
})

print("Average age:", studentsReal["age"].mean())

print("\nGender distribution:")
print(studentsReal["gender"].value_counts())

passing_rate = (studentsReal["passed"] == "Yes").mean() * 100
print("\nPassing percentage:", round(passing_rate, 2), "%")

print("\nAverage study time for those who passed vs failed:")
print(studentsReal.groupby("passed")["hours_studied"].mean())

#meore
df = pd.DataFrame(students)

X = df[["age", "hours_studied"]]

y = df["passed"]

print("X (inputs):\n", X, "\n")
print("y (output):\n", y, "\n")

df["attendance"] = [random.randint(50, 100) for _ in range(num_students)]

print("UPDATED DATAFRAME:\n", df, "\n")
X_new = df[["age", "hours_studied", "attendance"]]

print("X with attendance added:\n", X_new)