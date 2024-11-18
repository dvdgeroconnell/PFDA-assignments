# assignment_6_Weather.py
# 17/11 attempt

# Purpose of Program:
#   A program to...
# Now adding monthly mean of daily max.

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

pd.options.mode.copy_on_write = True

# Read the file, drop the first 23 header rows, and also the first data row as 4 months are missing after it
df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv", skiprows=23,low_memory=False)
df = df.drop(0)

df['datetime'] = pd.to_datetime(df['date'], format='%d-%b-%Y %H:%M')
df['datetime2'] = df['datetime']
df = df.set_index('datetime2')
# See how much data - number of rows and columns
print(df.shape)

# Set up the figure and axes
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16,8), sharex='col', sharey='row')
ax1 = axes[0,0]
ax2 = axes[0,1]
ax3 = axes[1,0]
ax4 = axes[1,1]

mean_daily_temp = df["temp"].resample("d").mean()
mean_monthly_temp = df["temp"].resample("m").mean()

# Draw the 3 plots - hourly temperature, daily mean temperature, monthly mean temperature
ax1.plot(df["datetime"], df["temp"])
ax1.plot(mean_daily_temp)
ax1.plot(mean_monthly_temp)
ax1.set_title('Full Dataset', fontsize=14)

# Need to cast the windspeed column to int - temporarily replace the bad data (whitespaces)
df['wdsp'] = df['wdsp'].replace(' ',-999)
df['wdsp2'] = df['wdsp']
df['wdsp2'] = df['wdsp2'].astype(int)
df['wdsp2'] = df['wdsp2'].replace(-999,np.nan)

# Number of samples in the moving window average (1 day / 24 hours)
moving_window_size = 24

# Rolling windspeed over a 24 hour moving window
rolling_windspeed = df['wdsp2'].rolling(moving_window_size).mean()

# Daily maximum windspeed
daily_max_windspeed = df["wdsp2"].resample("d").max()
df["max_wdsp"] = df["wdsp2"].resample("d").max()

# Monthly mean of daily max (the nasty bit)
monthly_mean_daily_max = df["max_wdsp"].resample("m").mean()

# Draw the 4 plots
ax3.plot(df['datetime'], df['wdsp2'])
ax3.plot(rolling_windspeed)
ax3.plot(daily_max_windspeed)
ax3.plot(monthly_mean_daily_max)

# ***********************************************************************
# * Create a set of plots for 2024 so we can see what 1 year looks like *
# ***********************************************************************

# Build a dataframe containing just 2024
dateFrom = "2024-01-01 00:00:00"
dateTo = "2024-12-31 23:00:00"
df_latest = df.loc[dateFrom:dateTo]
mean_daily_temp_latest = df_latest["temp"].resample("d").mean()
mean_monthly_temp_latest = df_latest["temp"].resample("m").mean()

# Draw the 3 plots - hourly temperature, daily mean temperature, monthly mean temperature
ax2.plot(df_latest["datetime"], df_latest["temp"])
ax2.plot(mean_daily_temp_latest)
ax2.plot(mean_monthly_temp_latest)
ax2.set_title('Latest Year', fontsize=14)

# rolling windspeed over a 24 hour moving window
rolling_windspeed_latest = df_latest['wdsp2'].rolling(moving_window_size).mean()
daily_max_windspeed_latest = df_latest["wdsp2"].resample("d").max()
df_latest["max_wdsp"] = df_latest["wdsp2"].resample("d").max()
monthly_mean_daily_max_latest = df_latest["max_wdsp"].resample("m").mean()
ax4.plot(df_latest["datetime"],df_latest["wdsp2"])
ax4.plot(rolling_windspeed_latest)
ax4.plot(daily_max_windspeed_latest)
ax4.plot(monthly_mean_daily_max_latest)

count_nan = df_latest['wdsp2'].isnull().sum()
print("Null count: ",count_nan)

xlabels = ["Hourly Temp","Daily Avg","Monthly Avg"]
wdlabels = ["Windspeed","Rolling Windspeed","Max Windspeed", "Monthly Mean of Daily Max"]

#plt.xticks(rotation=90)
plt.suptitle('Assignment 6', fontsize=16)
plt.tight_layout(rect=(0, 0.1, 1, 1))
ax1.legend(bbox_to_anchor=(0, 1), loc='upper left', labels=xlabels)
ax2.legend(bbox_to_anchor=(0, 1), loc='upper left', labels=xlabels)
ax3.legend(bbox_to_anchor=(0, 1), loc='upper left', labels=wdlabels)
ax4.legend(bbox_to_anchor=(0, 1), loc='upper left', labels=wdlabels)

plt.show()