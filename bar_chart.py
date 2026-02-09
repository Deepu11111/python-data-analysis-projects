import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print(df)

# 1. Bar chart analysis by categories
plt.figure()

plt.bar(df["Product"],df["Sales"])
plt.title("Sales by Product Category")
plt.xlabel("Product")
plt.ylabel("Sales (rs)")
plt.grid(True)

plt.show()

