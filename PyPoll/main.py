# Import the os module. OS will allow us to create file path to access the csv file
import os

# Import csv module to read CSV file in python once it is located by OS
import csv

# Create the file path (using os) to access the csv file (csv_path ='.\Resources\election_data.csv'). Path MUST start from the current location.
csv_path = os.path.join('.\Resources', 'election_data.csv')

# Read the csv file using csv module
with open(csv_path) as file:

    # Open the file using csv.reader, specifing variable that holds contents and the delimiter  
    csvreader = csv.reader(file, delimiter=',')

    # To separate the header (first line) from the data set, use next function; we can print to confirm
    csv_header=next(csvreader)
    
    # Set variables for data analysis, creat one list for unique candidate names and another with all the repeated names of candidate. We will use the repeated name list for finding the count of votes each unique candidate received since every repeat will be a vote count.
    numVotes = 0
    candidateName = "" 
    candidatesUniqueNameList = []
    candidatesRepeatNamesList = []
        
    # Loop through to read the data; we can print to confirm the list
    for line in csvreader:
        
        # Increment the vote count to track the total number of votes casted during the poll.
        numVotes = numVotes + 1
                
        # First create a list (candidatesRepeatNames List) which will have all the repeates of candidate names present in the file. Then to find the list of all the unique candidates who received votes in poll, check if that candidate exists in CandidatesUniqueName List. If not (unique), add to the list.
        candidateName = line[2]
        candidatesRepeatNamesList.append(candidateName)
        if candidateName not in candidatesUniqueNameList:
            candidatesUniqueNameList.append(candidateName)

# Set up variables for Output list (will include candidate name, percentage of votes received by each candidate, total votes received by each candidate) and the winner candidate.
outputList = []
winnerVoteCount = 0
winnerName =""

for candidateName in candidatesUniqueNameList:
    candidateInfoList =[]

    # First, add candidate name to the list
    candidateInfoList.append(candidateName)

    # Second, calculate and add percentage of votes each candidate recieved to the list
    candidateInfoList.append(candidatesRepeatNamesList.count(candidateName)/numVotes*100)

    # Third, calculate and add total number of votes each candidate recieved to the list
    candidateInfoList.append(candidatesRepeatNamesList.count(candidateName))

    # Add all the above information for each candidate to the output list
    outputList.append(candidateInfoList)

    # To find the winner, compare winnerVoteCount (initially set to 0) to the vote count for the current candidate and set winnerVoteCount and winnerName accordingly
    if (candidatesRepeatNamesList.count(candidateName) > winnerVoteCount):
        winnerVoteCount = candidatesRepeatNamesList.count(candidateName)
        winnerName = candidateName

# Create and add to textToPrint variable so that we can export results to output.txt in Analysis folder and print to console
textToPrint = 'Election Results\n'
textToPrint += "--------------------------\n"
textToPrint += (f"Total Votes: {numVotes}\n")
textToPrint += "--------------------------\n"

# When printing candidate info from output list, round the percentage vote to 3 decimals
for item in outputList:   
    textToPrint += (f"{item[0]}: {round(item[1], 3)}% ({item[2]})\n")
    
# Print winner name
textToPrint += "--------------------------\n"
textToPrint += (f"Winner: {winnerName}\n")
textToPrint += "--------------------------\n"

# Output textToPrint variable to output.txt file
with open("Analysis/output.txt","w") as txt_file:
    txt_file.write(textToPrint)

print(textToPrint)