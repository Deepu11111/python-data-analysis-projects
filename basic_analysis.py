import pandas as pd

df  = pd.read_csv("data.csv")

total_sales = df["Sales"].sum()
avg_tmp = df["Temperature"].mean()
total_expense = df["Expense"].sum()

print("Total Sales :",total_sales)
print("Average Temperature:",avg_tmp)
print("Total expense:",total_expense)