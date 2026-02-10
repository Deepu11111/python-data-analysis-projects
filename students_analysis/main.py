import pandas as pd
import matplotlib.pyplot as plt

# 1.Load Data

df = pd.read_csv("data/students.csv")

print("Data Set loaded successfully..")

print("First 5 rows: \n")
print(df.head())

print("\nColumns: ")
print(df.columns)

print("\nShape(row,columns): ")
print(df.shape)


# 2. Data Cleaning

print("\nChecking Missing Values: \n")
print(df.isnull().sum())

print("\nChecking Duplicates : ")
print(df.duplicated().sum())

# Revome exixsting duplicates if is there any 
df.drop_duplicates(inplace=True)

# ensure numeric columns are numeric
cols = ["Maths","Science","English","Attendance"]
df[cols] = df[cols].apply(pd.to_numeric)

print("\nData types : \n")
print(df.dtypes)

print("\nData Cleaned Successfully..")

# 3.Basic Analysis
print("\n======= BASIC ANALYSIS========\n")

math_avg = df["Maths"].mean()
science_avg = df["Science"].mean()
english_avg = df["English"].mean()

print("Maths Average :",round(math_avg,2))
print("Science Average :",round(science_avg,2))
print("English Average :",round(english_avg,2))

# Overall Avg per student
df["Total"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

class_avg = df["Average"].mean()
print("\nClass Overall Average:",round(class_avg,2))

# Topper Student 
topper = df.loc[df["Total"].idxmax()]
print("\nTopper Student",topper["Name"],"with total marks:" ,topper["Total"])

# Gender Count
print("\nGender Distribution:\n")
print(df["Gender"].value_counts())

# 4.1. Visualization Bar Chart
subjects = ["Maths","Science","English"]
averages = [math_avg,science_avg,english_avg]

plt.figure()
plt.bar(subjects,averages)

plt.title("Subject wise average marks...")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.grid(True)
plt.savefig("visualizations/subject_average_bar.png")
plt.show()

# 4.2 Visualizations Pie Chart
gender_counts = df["Gender"].value_counts()

plt.figure()

plt.pie(gender_counts,
    labels = gender_counts.index,
    autopct = "%1.1f%%")

plt.title("Average Distribution")
plt.axis('equal')

plt.savefig("visualizations/gender_distribution_pie.png")
plt.show()

# 4.3. Generate Report File

report_text = f"""
===== STUDENT PERFORMANCE REPORT =====

Total Students: {len(df)}

Subject Averages:
Maths: {round(math_avg,2)}
Science: {round(science_avg,2)}
English: {round(english_avg,2)}

Class Overall Average: {round(class_avg,2)}

Topper Student: {topper['Name']} (Total Marks: {topper['Total']})

Gender Distribution:
{df['Gender'].value_counts().to_string()}

===== INSIGHTS =====
1. Science has the highest average marks.
2. The class performance is above 70% overall.
3. Top students scored above 90 in most subjects.
4. Gender distribution is balanced.

Charts saved inside 'visualizations/' folder.
"""

with open("report/report.txt", "w", encoding="utf-8") as f:
    f.write(report_text)


print("\nReport generated successfully → report/report.txt")


