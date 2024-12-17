
# Repository - PFDA-assignments

  
   
| Topic | Details |
|---------|-------------|
| **Module:**  | 4369 - Programming for Data Analytics  |
| **Lecturer:**  | Andrew Beatty  | 
| **Course:**  | Higher Diploma in Science in Computing (Data Analytics)  |
| **Year/Semester:**  | Year 1 / Semester 2  |
| **Student Name:**  | David O'Connell  |
| **Student ID:**  | G00438912  |
| **Student Email:**  | G00438912@atu.ie  |  

## Purpose of this Repository  
This is the GitHub repository for the assignments associated with the Programming for Data Analytics module.   
Link to repository - [PFDA Assignments](https://github.com/dvdgeroconnell/PFDA-assignments.git).
   
## About this README  
This README contains an overview of the purpose, contents and instructions for use of the *PFDA-assignments* repository.  
  
It has been based on the guidelines in [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).  
  
More information on writing in Markdown can be found in [Github's documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). 

## Assignments and Associated Content in this Repository

### Assignment 1  
**Assignment:** Upload the URL to the PFDA assignment repository.  
  
The URL is - https://github.com/dvdgeroconnell/PFDA-assignments.git  

### Assignment 2  
**Assignment:** Create a jupyter notebook called *assignment2-weather.ipynb* with a plot of the "dryBulbTemperature_Celsius" field over time.  
  
The *assignment2-weather.ipynb* response is contained in this repository.  

### Assignment 3  
**Assignment:** Create a notebook called *assignment03-pie.ipynb* with a pie chart of people's email domains in the csv file at the url https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download. This csv file has 1000 people.  
  
The *assignment03-pie.ipynb* response is contained in this repository. A link to the data is used in the notebook, but it is also downloaded to the file *people-1000.csv* in case the network-based file is not available when the notebook is being run - simply switch the `read_csv()` command to the local file.  

### Assignment 4  
**Assignment:** There was no assignment 4.  

### Assignment 5  
**Assignment:** Create a Python program (or notebook) called *assignment_5_risk* (*.py* or *.ipynb*). Calculate the outcome of either:
- A user-provided number of individual battle rounds in the game Risk; and plot the total attackers and total defenders lost in a pie chart.  
- Calculate a random number of attackers and defenders, and run until one or the other is depleted to zero. The attack and defence losses after each round are plotted in a line graph.  
  
The *assignment_5_risk.py* program is contained in this repository. It is run by executing the command `python assignment_5_risk.py` from the command line.  

### Assignment 6
**Assignment:** Create a Python program (or notebook) called *assignment_6_Weather* (*.py* or *.ipynb*) to retrieve weather data from https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv and to plot:  
  a) For 60%  
     - The temperature  
     - The mean temperature each day  
     - The mean temperature for each month  
  b) For an additional 40%  
     - The Windspeed (data missing from this column)  
     - The rolling windspeed over 24 hours  
     - The max windspeed for each day  
     - The monthly mean of the daily max windspeeds  
   
The *assignment_6_Weather.py* program is contained in this repository. It is run by executing the command `python .\assignment_6_Weather.py` from the command line. One figure with 4 individual plots is drawn. Note that it is processing a large amount of data and may take a few seconds to run.  

### Other Files  
  
#### people-1000.csv  
This file contains a list of 1000 fictitious people and their details. It exists as a local input file for the *assignment03-pie.ipynb* notebook.  

#### weatherreadings1.csv  
This is the input file for the *assignment2-weather.ipynb* notebook.  
  
#### .gitignore  
This is the .gitignore file generated by GitHub at time of repository creation, and instructs GitHub on which files to ignore when uploading the local version of the repository.  

#### requirements.txt  
This is the output of the `pip freeze` command, listing all of the packages and dependencies in the Python environment.  
  
# References
For support with coding questions, the following sites were the most widely used:  
- https://www.stackoverflow.com/  
- https://www.w3schools.com/  
- https://www.geeksforgeeks.org/  
- https://www.datacamp.com/  

### End