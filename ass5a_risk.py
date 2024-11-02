# assignment_5_risk.py

# A program to calculate the outcome of a user-provided number of individual battle rounds 
# in the game Risk; and to plot the total attackers and total defenders lost in a pie chart.

# Summary of Rules
# In each battle round the attacker can put forward up to 3 troops (3 dice), and the defender
# can put forward up to 2 troops (2 dice).
# The 2 highest of the 3 attacking dice are used.
# The top 2 dice are compared and the attacker wins if their throw is greater than the defender's,
# who loses a troop). Otherwise attack loses a troop.
# The next 2 highest are then compared and the attacker wins if their throw is greater than the
# defender's, who loses a troop). Otherwise attack loses a troop.

# Assumptions: 3 attackers and 2 defenders available and committed in each round

# Author: David O'Connell

# References:
#  PFDA Topic 5 lecture videos (Andrew Beatty) - https://vlegalwaymayo.atu.ie/course/view.php?id=10462
#  https://www.w3schools.com/python/numpy/default.asp for NumPy
#  https://www.w3schools.com/python/numpy/numpy_random.asp for randon integer generation
#  https://www.w3schools.com/python/matplotlib_pie_charts.asp for pie charts
#  https://www.geeksforgeeks.org/python-ways-to-add-row-columns-in-numpy-array/ to add rows to a 2D array
#  https://stackoverflow.com/questions/4001067/sum-one-row-of-a-numpy-array to sum a row in a 2D array

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

attack_army = np.random.randint(100, 10000)
defence_army = np.random.randint(100, 10000)
print("Attack army is",attack_army)
print("Defence army is",defence_army)

count = 0
result = np.array([count,attack_army,defence_army, 0, 0])

while ((attack_army > 0) and (defence_army > 0)):
    attack = np.random.randint(1, 7, (1,3))
    # order each row descending and slice the leftmost 2 columns (best results)
    attack[:,::-1].sort()
    attack = attack[:,0:2]
    defence = np.random.randint(1, 7, (1,2))
    # order each row descending
    defence[:,::-1].sort()
    defender_losses = (attack > defence).sum()
    #print("defender losses ",defender_losses)
    attacker_losses = 2-defender_losses
    #print("attacker losses ",attacker_losses)

    # Finish it off
    defence_army -= defender_losses
    if defence_army < 0:
        defence_army = 0
    attack_army -= attacker_losses
    if attack_army < 0:
        attack_army = 0
    count+=1
    new_row=np.array([count, attack_army, defence_army, attacker_losses, defender_losses])
    result = np.vstack((result, new_row))
    #print ("new result = ", result[count])

print("Remaining attackers after",count,"rounds =",attack_army)
print("Remaining defenders after",count,"rounds =",defence_army)

print (result)
plt.plot(result[0:count+3, 1])
plt.plot(result[0:count+3, 2])

# Adjust the x-scale
plt.xlim([0, max(result[0:count,0])])
max1 = max(result[0:count,1])
max2 = max(result[0:count,2])

# adjust the y-scale
max = max1
if max2 > max:
    max = max2
max = max*1.1
plt.ylim([0, max])

risk_title = "Risk Results for " + str(count) + " rounds"
risk_labels = ["Attack","Defence"]
plt.title(risk_title, loc='left', fontsize=14)
plt.legend(bbox_to_anchor=(1.02, 1.15), loc='upper right', labels=risk_labels)
plt.show()