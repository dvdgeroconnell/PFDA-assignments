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

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

def do_menu():
    # Ask for a value and check that it is an integer - handle range checking in the main program
    try:
        choice = int(input("\nEnter the number of rounds, up to 1 million (0 to quit): "))
    # Handle non-integer entries gracefully
    except ValueError:
        print("Invalid entry, not an integer")
        choice = 0
    return choice

total = do_menu()

if total > 1000000:
    print("Be reasonable")

elif total > 0:
    attack = np.random.randint(1, 7, (total,3))
    # order each row descending and slice the leftmost 2 columns (best results)
    attack[:,::-1].sort()
    attack = attack[:,0:2]
    #print ("attack is\n",attack)

    defence = np.random.randint(1, 7, (total,2))
    # order each row descending
    defence[:,::-1].sort()
    #print ("defence is\n",defence)

    # Now do a boolean compare on the 2 to get the results... result will be true if the
    # remaining highest attacker throw is HIGHER than the remaining highest defence throw.
    # If it is LOWER THAN or EQUAL TO the, the result will be FALSE. So TRUE will equate
    # to a defence loss
    defender_losses = (attack > defence)
    #print("result by row is \n", defender_losses)

    result_of_each_round = np.zeros(total)
    x = 0
    while x < total:
        result_of_each_round[x] = sum(defender_losses[x, 0:2])
        x +=1

    # Sum up the defender losses
    defenders_lost = int(sum(result_of_each_round))
    attackers_lost = int(total*2-defenders_lost)
    print("attackers lost: ", attackers_lost)
    print("defenders lost: ", defenders_lost)

    # Draw a pie chart of the results
    risk_result = [attackers_lost,defenders_lost]
    # Add totals to the legend, pie chart shows percentages
    risk_labels = ["Attack Loss: " + str(attackers_lost),"Defence Loss: " + str(defenders_lost)]
    explode=[0.05, 0.05]
    plt.pie(risk_result, labels = None, autopct='%1.1f%%', explode=explode)
    risk_title = "Risk results for " + str(total) + " rounds"
    plt.title(risk_title)
    plt.legend(bbox_to_anchor=(1.0, 0.6), loc='upper left', labels=risk_labels)
    plt.subplots_adjust(right=0.6)
    plt.show()
