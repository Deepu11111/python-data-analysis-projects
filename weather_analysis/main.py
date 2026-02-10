import pandas as pd
import matplotlib.pyplot as  plt

try:

# Data Load
 df = pd.read_csv("data/weather.csv")
 print("\nData Loaded Successfully\n")

 # show first rows
 print(df.head())

 # basic info
 print("\nColumns:")
 print(df.columns)

 print("\nShape (rows,columns):",df.shape)

except FileNotFoundError:
 print("\nFile not found in data folder...")

# Data Cleaning
print("\nCleaning Data..\n")

#convert date column to datetime
df["Date"] = pd.to_datetime(df["Date"],errors="coerce")

# Convert numeric columns
cols = ["Temperature","Humidity","Rainfall"]
df[cols] = df[cols].apply(pd.to_numeric,errors="coerce")

# Check missing values
print("Missing values:\n",df.isnull().sum())

# Drop missing rows
df = df.dropna()
print("\nAfter cleaning shape:",df.shape)

print("\nCleaning Completed\n")

# Weather Basic Analysis 

print("\nPerforming Analysis..\n")
avg_temp = df["Temperature"].mean()
max_temp = df["Temperature"].max()
min_temp = df["Temperature"].min()
total_rain = df["Rainfall"].sum()
avg_humidity = df["Humidity"].mean()

print(f"Average Teamperature: {avg_temp:.2f}")
print(f"Maximum Temperature: {max_temp}")
print(f"Minimum Temperature :{min_temp}")
print(f"Total Rainfall: {total_rain}")
print(f"Average Humidity: {avg_humidity:.2f}")

# Line Chart(Temperature)
print("\n Creating Temperature Line Chart..\n")

plt.figure(figsize=(8,5))
plt.plot(df["Date"],df["Temperature"],marker="o")

plt.title("Temperature Treand Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (deg C)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visualizations/temperature_trend.png")
plt.show()

print("\ntemperature_trend.png saved inside visualizations folder")

# Bar Chart 
print("\nCreating Rainfall Bar Chart...\n")

plt.figure(figsize=(8,5))
plt.bar(df["Date"].dt.strftime("%d-%b"),df["Rainfall"])
plt.title("Daily Rainfall Comparison")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("visualizations/rainfall_bar.png")
plt.show()

print("\n rainfall_bar.png saved in visualizations folder")

# Generate Text Report
print("\n Generating Report..\n")

report_text = f"""
======== Weather Data Analysis Report ========

Total Records: {len(df)}

Average Temperature: {avg_temp:.2f} °C
Maximum Temperature: {max_temp} °C
Minimum Temperature: {min_temp} °C

Total Rainfall: {total_rain} mm
Average Humidity: {avg_humidity:.2f} %

Insights:
- Temperature shows daily fluctuations across the week
- Rainfall occurred only on a few days
- Weather mostly dry with moderate humidity
- Suitable for trend-based forecasting

Charts Generated:
- temperature_trend.png
- rainfall_bar.png
"""

with open("report/weather_report.txt", "w", encoding="utf-8") as f:
    f.write(report_text)

print("\nweather_report.txt saved inside report folder")