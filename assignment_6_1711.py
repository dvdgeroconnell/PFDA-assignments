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
#
#
# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as figure
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns

# Read the file, drop the first 23 rows as they are header data, then also drop the first row
# of data as there are nearly 4 months of data missing after it
df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv", skiprows=23,low_memory=False)
df = df.drop(0)

df['datetime'] = pd.to_datetime(df['date'], format='%d-%b-%Y %H:%M')
df['datetime2'] = df['datetime']
df = df.set_index('datetime2')
df['yr'] = pd.DatetimeIndex(df['datetime']).year
df['day'] = pd.DatetimeIndex(df['datetime']).day
print(df.head(18))
print(df.tail(5))

#******************

mean_daily_temp = df["temp"].resample("d").mean()
print(mean_daily_temp.head(1))
print(mean_daily_temp.tail(1))
mean_monthly_temp = df["temp"].resample("m").mean()
print(mean_monthly_temp.head(1))
print(mean_monthly_temp.tail(1))

plt.plot(df["datetime"], df["temp"])
plt.plot(mean_daily_temp)
plt.plot(mean_monthly_temp)

plt.xticks(rotation=90)
plt.tight_layout(rect=(0, 0.1, 1, 1))
plt.show()

#******************
dateFrom = "2010-01-01 01:00:00"
dateTo = "2011-01-01 01:00:00"
df.loc[dateFrom:dateTo]['meant'].mean()
 