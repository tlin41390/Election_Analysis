import os
import csv
def main():

    #The data needed to be retrieved from 
    #1.Total number of votes cast
    #2.complete list of candidates who received votes
    #3.percentage of votes each candidate won
    #4.stotal number of votes for each candidate won
    #5.winner of election based on the popular vote

    #create a filename variable to a direct or indirect path to the file

    #Assign a variable to save in a file from a path
    file_to_save = os.path.join("analysis","election_analysis.txt")

    #Assign a file to load a file from the path
    file_to_load = os.path.join("Resources","election_results.csv")

    #Using  the with statement open the file as a text file
    with open(file_to_save,"w") as txt_file:
        #writes the counties to the text file
        txt_file.write("Counties in the election\n")
        txt_file.write("-------------------------\n")
        txt_file.write("Arapahoe\nDenver\nJefferson")

    numVotes = 0
    #Initialized empty array of candidate.
    candidate_options = []

    #Initialize empty dictionary.
    candidate_votes = {}

    #Winning count, percentage and candidate
    winning_count = 0
    winning_candidate =""
    winning_percentage=0

    with open(file_to_load) as election_data:
        #Read and analyze the data here
        file_reader = csv.reader(election_data)
        #print the rows of the file
        headers =next(file_reader)
        print(headers)

        for row in file_reader:
            #Get the total num of candidates
            candidate_names= row[2]
            #Get the total number of votes
            numVotes+=1

            #Append the candidate names
            if candidate_names not in candidate_options:
                candidate_votes[candidate_names]=0
                candidate_options.append(candidate_names)
            candidate_votes[candidate_names]+=1

        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            votePercentage = (float(votes)/float(numVotes)*100)
            print(f"{candidate_name}: {votePercentage:.1f}% ({votes:,})")
            if(votes>winning_count) and(votePercentage>winning_percentage):
                winning_count = votes
                winning_percentage = votePercentage
                winning_candidate = candidate_name
        winning_candidate_summary = (
            f"--------------------------------\n"
            f"winner: {winning_candidate}\n"
            f"winning count: {winning_count:,}\n"
            f"winning percentage: {winning_percentage:.1f}%\n"
            f"--------------------------------"
        )
        print(winning_candidate_summary)

main()
