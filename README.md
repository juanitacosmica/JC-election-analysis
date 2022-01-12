# JC-election-analysis
Module 3, intro to Python!



# Project Overview
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.1, VS Code 1.63.2

## Summary
The analysis of the election showed that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received "23%" of the vote and 85,123 number of votes.
    - Diana DeGette received "74%" of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received "3%" of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette (Candidate 2), who received "74%" of the vote and 11,606 number of votes.

## Election-Audit Summary: 

The Election Commision could benefit from this Python Script for any election by simply providing the data in a .csv file. Containing:
- Candidate names
- Counties
- Number of votes

All sort of calculations can be performed around it, the current script counts number of votes per county and per candidate, and calculates percentages; therefore, it is capable to define the winner (candidate and/or county) and shows as well the county with the largest turnout.This last portion was achieved through the following:

![Calculation Capabilities of this Script](/Resources/code_image_4.png)

The script will fetch the data (called from the lists and dictionaries) and run the calculations using our variables once the file is placed in the proper directory and connected to the code:

![Connect the data to the script](/Resources/code_image_1.png)

This data will give the information required to run the script to print the results: per county and/or per candidate, what changes is the variables we define and the calculations we decide to print, which can be easily tailored as per the results we need to populate.

Results per Candidate:
![Results per Candidate](/Resources/code_image_3.png)

vs Results per Candidate and County:
![Results per Candidate and County](/Resources/code_image_2.png)

The results from this case scenario, where the calculation was made to see the Winning candidate and county, is shown like follows:

![Final Results](/Resources/challenge_results.png)
