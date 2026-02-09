import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data

df = pd.read_csv("data.csv")
print("Data Set loaded :\n")
print(df)

# 2. Clean Data


df.dropna(inplace=True)
df.columns=df.columns.str.strip()

# 3.Analysis of Numbers

total_sales = df["Sales"].sum()
avg_temp = df["Temperature"].mean()
total_expense = df["Expense"].sum()

print("\n=======Final Report=======")
print("Total Sales:",total_sales)
print("Average Temperature:",avg_temp)
print("Total Expense:",total_expense)

# 4.Bar Chart Analysis

plt.figure()
plt.bar(df["Product"],df["Sales"])
plt.title("Sales by Product Category")
plt.xlabel("Product")
plt.ylabel("Sales  (rs)")
plt.grid(True)
plt.show()

# 5. Line Chart Analysis
plt.figure()
plt.plot(df["Month"],df["Temperature"],marker='o')
plt.title("Monthly Temperature Trend")
plt.xlabel("Month")
plt.ylabel("Temperature (deg C)")
plt.grid(True)
plt.show()

# 6. Pie Chart Analysis
plt.figure()
plt.pie(df["Expense"],labels=df["Month"],autopct="%1.1f%%")
plt.title("Monthly Expense Distribution")
plt.axis('equal')
plt.show()