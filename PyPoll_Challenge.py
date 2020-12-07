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
    
def fileReader(fileLoad,fileSave):

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


    with open(fileSave, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        print(election_results, end="")
        txt_file.write(election_results)
        
        for counties in countyVotes:
            getVotes = countyVotes.get(counties)
            countyPercentage = float(getVotes)/float(total_votes)*100
            countyResults = (f"{counties}: {countyPercentage:.1f}% {getVotes:,}\n")
            print(countyResults)
            txt_file.write(countyResults)
            global winningVotes
            global winningPercentage
            if(getVotes>winningVotes) and(countyPercentage>winningPercentage):
                winningVotes = getVotes
                winningPercentage=countyPercentage
                winningCounty = counties
                turnoutCounty = (f"-------------------------\n"
                                f"Largest County Turnout: {counties}\n"
                                f"--------------------------\n")
        print(turnoutCounty)
        txt_file.write(turnoutCounty)


        for candidate_name in candidate_votes:
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            print(candidate_results)
            txt_file.write(candidate_results)

            # Determine winning vote count, winning percentage, and candidate.
            global winning_count
            global winning_candidate
            global winning_percentage
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage

        # Print the winning candidate (to terminal)
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

def main():
    fileReader(file_to_load,file_to_save)
    

main()

