import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print(df)

# 2. Line chart analysis 

plt.figure()
plt.plot(df["Month"],df["Temperature"],marker ='o')
plt.title("Monthly Temperature Trend")
plt.xlabel("Month")
plt.ylabel("Temperature (d.celc)")
plt.grid(True)

plt.show()