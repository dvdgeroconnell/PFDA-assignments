# assignment_6_Weather.py

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
print(df.head(3))

# or you could use this to drop the first row
# dateFrom = "2010-01-01 01:00:00"
# dateTo = "2011-01-01 01:00:00"
# sns.lineplot(data=df.loc[dateFrom:dateTo], x="date", y="meant")

df['date_time'] = pd.to_datetime(df['date'], format='%d-%b-%Y %H:%M')
df['yr'] = pd.DatetimeIndex(df['date_time']).year
# Set the index to date
df.head(3)
#date2 = 
df = df.set_index('yr')
df.head(3)

# instead of truncate, could also use plot = sns.lineplot(data=df.iloc[1:12], x="date", y="temp")
new = df.truncate(after=25000, axis=0, copy=True) 
print(new.head(3))

'''
fig = plt.figure(figsize=(10, 5)) 
# creating the bar plot 
plt.bar(names, age, color='blue', width=0.4) 
plt.xlabel("Names")
g.set_xticklabels( 
    labels=["Asia", "Africa", "Antartica", "Europe"], rotation=30)  
plt.ylabel("Age of the person") 
plt.show()
'''

#plot = sns.lineplot(data=new, x="datetime", y="temp")
plot = sns.lineplot(data=new["temp"])
plt.figure(figsize=(8, 6))

#sns.set_context("notebook", rc={"figure.figsize": (15, 10)})
#plt.rcParams['figure.figsize']=2,1
plot.set_xticklabels(labels=new["date_time"],rotation=90)
#plot.set_xticks(ticks=new["yr"])
#plot.set_xticklabels(labels=new["yr"], rotation=90)
#plot.set_xticks([0, 1, 2, 3])
#plot.set_xticklabels(["1996", "1997", "1998", "1999"])
#plot.xaxis.set_major_locator(ticker.LinearLocator(7600))
plt.show()

'''
        # Draw a pie chart of the results
        risk_result = [attack_losses,defence_losses]
        # Add totals to the legend, pie chart shows percentages
        risk_labels = ["Attack Loss: " + str(attack_losses),"Defence Loss: " + str(defence_losses)]
        explode=[0.05, 0.05]
        plt.pie(risk_result, labels = None, autopct='%1.1f%%', explode=explode)
        risk_title = "Risk results for " + str(rounds) + " rounds"
        plt.title(risk_title)
        plt.legend(bbox_to_anchor=(1.0, 0.6), loc='upper left', labels=risk_labels)
        plt.subplots_adjust(right=0.6)
        plt.show()
    return

    # Adjust the x-scale
    plt.xlim([0, max(result[0:count,0])])
    max1 = max(result[0:count,1])
    max2 = max(result[0:count,2])

    # adjust the y-scale
    maxx = max1
    if max2 > maxx:
        maxx = max2
    maxx = maxx*1.1
    plt.ylim([0, maxx])

    title_str = "Result: Attack loses"

    risk_title = "Risk Results for " + str(count) + " rounds"
    risk_labels = ["Attack","Defence"]
    plt.suptitle(risk_title, fontsize=14)
    plt.title(title_str, loc='left')
    plt.legend(bbox_to_anchor=(1.02, 1.15), loc='upper right', labels=risk_labels)
    plt.show()
'''