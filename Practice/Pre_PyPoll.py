#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#to connect to the file, use: Resources\election_results.csv
# Import the datetime class from the datetime module.
import csv
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
# Assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'
#Open the election results and read the file.
election_data = open(file_to_load, 'r')
#To Do: perform analysis.

#Close the file.
election_data.close()
#Open the election results and read the file
with open(file_to_load) as election_data:
    #To Do: perform analysis
    print(election_data)
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load=os.path.join("Resources","election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    #Print the file object.
    print(election_data)
#Create a filename variable to a direct or indirect path to the file.
file_to_save=os.path.join("analysis","election_analysis.txt")
#Using the open() function with the "w" mode we will write data to the file.
#outfile=open(file_to_save,"w")
#Write some data to the file.
#outfile.write("Hello World")
#Close the file
#outfile.close()
#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    #Write some data to the file.
    #txt_file.write("Hello World")
    #txt_file.write("Araphoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    #Another method: txt_file.write("Arapahoe, Denver, Jefferson")
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
# Open the election results and read the file:
with open(file_to_load) as election_data:
    # To Do: read and analyze the dara here.
    file_reader=csv.reader(election_data)
    #Print each row in the CSV file.
    for row in file_reader:
        print(row)
    #Print the header row.
    headers=next(file_reader)
    print(headers)
       