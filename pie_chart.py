import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
print(df)

plt.figure()

plt.pie(
    df["Expense"],
    labels=df["Month"],
    autopct= "%1.1f%%"
)

plt.title("Monthly Expense Distribution")

plt.show()