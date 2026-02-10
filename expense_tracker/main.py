import pandas as pd
import matplotlib.pyplot as plt

try:

# Load dataset

 df = pd.read_csv("data/expenses.csv")
 print("\nData loaded Successfully\n")

 print(df.head())
 print("\nColumns:")
 print(df.columns)

 print("\nShape:",df.shape)

except FileNotFoundError:
 print("\nexpenses.csv not found inside data folder")


 # Data Cleaning
print("\n Cleaning Data..\n")

#Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"],errors="coerce")

# Convert Amount To Numeric 
df["Amount"] = pd.to_numeric(df["Amount"],errors="coerce")

# Check missing values
print("Missing values:\n",df.isnull().sum())

# Drop missing Rows
df = df.dropna()

print("\nAfter cleaning shape:",df.shape)

print("\nCleaning completed\n")

# Expense Analysis

print("\n Performing Expense Analysis..\n")

total_expense = df["Amount"].sum()
avg_expense = df["Amount"].mean()
max_expense = df["Amount"].max()

print(f"Total Expense:{total_expense}")
print(f"Average Expense: {avg_expense:.2f}")
print(f"Highest Single Expense:{max_expense}")

# Category wise totals
category_totals = df.groupby("Category")["Amount"].sum()

print("\nCategory-wise Expense:\n")
print(category_totals)


# BAR CHART
print("\n Creating Category Spending Bar Chart..\n")
plt.figure(figsize=(8,5))

plt.bar(category_totals.index,category_totals.values)
plt.title("Category-wise Expense Comparison")
plt.xlabel("Category")
plt.ylabel("Total Amount")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visualizations/category_spending_bar.png")
plt.show()
print("category_spending_bar.png saved")

# PIE CHART
print("\n Creating Expense Distribution Pie Chart..\n")
plt.figure(figsize=(6,6))

plt.pie(
 category_totals.values,
 labels=category_totals.index,
 autopct="%1.1f%%",
 startangle=90
)

plt.title("Expense Distribution by Category")
plt.tight_layout()
plt.savefig("visualizations/expense_distribution_pie.png")
plt.show()
print("expense_distribution_pie.png saved")
