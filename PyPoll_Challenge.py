# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
countyList = []
countyVotes={}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

winningCounty=""
winningVotes = 0
winningPercentage=0

# Function will read through the election data in order to get the county, candidate, and the total votes 
# as well as build the county and candidate list and dictionary for future use
def fileReader(fileLoad):

    with open(fileLoad) as election_data:
        reader = csv.reader(election_data)
        header = next(reader)

        for row in reader:
            global total_votes
            total_votes +=1
            candidate_name = row[2]
            getCounty = row[1]

            if candidate_name not in candidate_options:
                candidate_options.append(candidate_name)
                candidate_votes[candidate_name] = 0

            candidate_votes[candidate_name] += 1

            if getCounty not in countyList:
                countyList.append(getCounty)
                countyVotes[getCounty] =0

            countyVotes[getCounty] += 1

def writeToTxt(fileSave):
    global txt_file
    with open(fileSave, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        print(election_results, end="")
        txt_file.write(election_results)

        county(countyVotes)
        candidates(candidate_votes)

        # Print the winning candidate (to terminal)
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

#Function wiill determine the total votes in one county, the percentage of votes for that county 
# and then print out the total county results
def county(countyVotes):
    for counties in countyVotes:
        getVotes = countyVotes.get(counties)
        countyPercentage = float(getVotes)/float(total_votes)*100
        countyResults = (f"{counties}: {countyPercentage:.1f}% {getVotes:,}\n")
        txt_file.write(countyResults)
        print(countyResults)

        global winningVotes
        global winningPercentage

        if(getVotes>winningVotes) and(countyPercentage>winningPercentage):
            winningVotes = getVotes
            winningPercentage=countyPercentage
            winningCounty = counties
            turnoutCounty = (f"-------------------------\n"
                            f"Largest County Turnout: {winningCounty}\n"
                            f"--------------------------\n")
            print(turnoutCounty)
    txt_file.write(turnoutCounty)

# Function that will take in the candidate dictionary to calculate results of total votes
# Total percentage and the candidate's resuluts as well as deciding who won the election.
def candidates(candidateVotes):
        for candidate_name in candidateVotes:
            votes = candidateVotes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100
            global candidate_results
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            txt_file.write(candidate_results)
            print(candidate_results)

            global winning_count
            global winning_candidate
            global winning_percentage

            # Determine winning vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage




def main():
    fileReader(file_to_load)
    writeToTxt(file_to_save)
    

main()

