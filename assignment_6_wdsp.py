# assignment_6_Weather.py
# 17/11 attempt

# Purpose of Program:
#   A program to...

# Assumptions:
#   List any assumptions here...

# Author: David O'Connell

# References:
#   PFDA Topic 56 lecture videos (Andrew Beatty) - https://vlegalwaymayo.atu.ie/course/view.php?id=10462
#   https://www.w3schools.com/python/numpy/default.asp for NumPy
#   https://www.geeksforgeeks.org/rotate-axis-tick-labels-in-seaborn-and-matplotlib/ for rotating labels
#
# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as figure
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
import sys

# Read the file, drop the first 23 rows as they are header data, then also drop the first row
# of data as there are nearly 4 months of data missing after it
df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv", skiprows=23,low_memory=False)
df = df.drop(0)

df['datetime'] = pd.to_datetime(df['date'], format='%d-%b-%Y %H:%M')
df['datetime2'] = df['datetime']
df = df.set_index('datetime2')
print(df.head(3))
print(df.tail(3))

mean_daily_temp = df["temp"].resample("d").mean()

mean_monthly_temp = df["temp"].resample("m").mean()

dateFrom = "2024-01-01 01:00:00"
dateTo = "2024-12-31 23:00:00"
df_latest = df.loc[dateFrom:dateTo]

df_latest["wdsp2"] = df_latest['wdsp'].astype(int)

windspeed = df_latest['wdsp2'].to_numpy()
np.set_printoptions(threshold=sys.maxsize)
print(windspeed)

print(df_latest.dtypes)
plt.plot(df_latest["datetime"],df_latest["wdsp2"])

#plt.xticks(rotation=90)
#plt.tight_layout(rect=(0, 0.1, 1, 1))

plt.show()
