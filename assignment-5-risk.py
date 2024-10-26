# assignment_5_risk.py
# Week 07 assignment 

# A program to read in a text file and print out the number of e's and E's it contains.
# It is assumed that both upper and lower case e's should be counted.

# 3 functions were written to see which appeared most efficient.
# - Read the whole file
# - Read a line at a time
# - Read a character at a time

# Author: David O'Connell

# References:
#  PANDS Topic 7 lecture videos - Andrew Beatty
#  https://github.com/andrewbeattycourseware/pands-course-material/blob/main/jupyternotebooks/topic07-files.ipynb
#  https://www.w3schools.com/python/ for string, file and exception handling
#  https://stackoverflow.com/questions/10140281/how-to-find-out-whether-a-file-is-at-its-eof


# We will need functions from the OS and sys modules
import os.path, sys

import numpy as np
import matplotlib.pyplot as plt

def throw_one_die():
    x = np.random.randint(1, 7, 1000)
    return x

attack = np.random.randint(1, 7, (1000,3))

# order each row and slice the leftmost 2 columns (best results)
attack[:,::-1].sort()
attack = attack[:,0:2]
print ("attack is\n",attack)

defence = np.random.randint(1, 7, (1000,2))
# order each row
defence[:,::-1].sort()
print ("defence is\n",defence)

# now do a boolean compare on the 2 to get the results...



'''
a = np.array([[1,7,5], [4,8,5], [7,5,6]])
print(a)

# b is a ascending
b = np.sort(a)
print("a ascending is\n",b)

sorted = np.sort(a)[:,::-1]
print("a descending is\n",sorted)

a[:,::-1].sort()
print("a reordered is\n",a)

c = a[:,0:2]
print("shorter a\n")
print(c)

#result = throw_one_die()
#plt.hist(result)
#print(result)
#plt.show()

# This function read a file into memory as a string, and counts the E's and e's.
# This appears to be an inefficient use of memory for large files.
# Better to read a line or character at a time.

def read_count_by_file(sourcefile):
    # We have already checked the filename, this checks it can be opened.
    try:
        # Open the file in text read mode as f.
        with open(sourcefile, "rt") as f:
            x = 0
            count = 0
            # Read the entire file into a string called 'content'.
            content = f.read()

            # Loop through the string, character by character.
            # x will be one less than the length since the index range is 0 to len-1.
            while x < len(content):
                # Increment the counter if an e or an E
                if content[x] == 'e' or content[x] == 'E':
                    count +=1
                x+=1
        # Return the count of e's and E's.
        return(count)
                
    # Return -1 if the file cannot be opened.
    except IOError:
        return(-1)


# This function read a file into memory line by line, and counts the E's and e's in each line.
# This is more efficient use of memory, but requires 2 loops, one to read each line and one to 
# count the e's and E's in that line - so the code is more complex.

def read_count_by_line(sourcefile):
    # We have already checked the filename, this checks it can be opened.
    try:
        # Open the file in text read mode as f.
        with open(sourcefile, "rt") as f:
            count=0
            for line in f:
                x=0
                chr = line[x]
                y = len(line)
                while (chr) and (x<y):
                    if chr == 'e' or chr == 'E':
                        count += 1
                    x += 1
                    if x<y:
                        chr = line[x]
        # Return the count of e's and E's.
        return(count)

    # Return -1 if the file cannot be opened.
    except IOError:
        return(-1)


# This function read a file character by character, and increments a counter if that character
# is an E or an e.
# This makes more efficient use of memory, and the code is simpler - perhaps there are performance
# implications in retrieving each character separately from the file as opposed to a string in memory.

def read_count_by_char(sourcefile):
    # We have already checked the filename, this checks it can be opened.
    try:
        # Open the file in text read mode as f.
        with open(sourcefile, "rt") as f:
            count = 0
            # Read one character.
            chr = f.read(1)
            # And increment the counter if it is an e or an E.
            while(chr):
                if chr == 'e' or chr == 'E':
                    count += 1
                chr = f.read(1)
        # Return the count of e's and E's.
        return(count)

    # Return -1 if the file cannot be opened.
    except IOError:
        return(-1)
    

# Main Program

# Check if a filename was provided as an argument. If not, print an error message and exit.
try:
    filename = sys.argv[1]

# If no filename provided, the exception returned is an IndexError.
except IndexError:
    print("Error - no file name was provided.")

else:
    # A filename was provided - check if it exists. If not, print an error and exit.
    if not os.path.isfile(filename):
        print("Error - not a valid file")

    # A valid filename has been provided. Count the e's and E's.
    else:

        # Read in the whole file and count the e's and E's in the string that the file is stored in.
        count_file = read_count_by_file(filename)
        # Check if the file could be opened.
        if count_file == -1:
            print("Error - that file cannot be opened")
        else:
            print(f"Reading in the whole file, the count of e's in {filename} is {count_file}")
        
        # Read the file a line at a time and count the e's and E's in the string that the line is stored in.
        count_line = read_count_by_line(filename)
        # Check if the file could be opened.
        if count_line == -1:
            print("Error - that file cannot be opened")
        else:
            print(f"Reading 1 line at a time, the count of e's in {filename} is {count_line}")
        
        # Read the file a character at a time and increment the counter if it's an e or an E.
        count_char = read_count_by_char(filename)
        # Check if the file could be opened.
        if count_char == -1:
            print("Error - that file cannot be opened")
        else:
            print(f"Reading 1 character at a time, the count of e's in {filename} is {count_char}")
'''