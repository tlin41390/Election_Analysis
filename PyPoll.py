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

    with open(file_to_load) as election_data:
        #Read and analyze the data here
        file_reader = csv.reader(election_data)
        #print the rows of the file
        headers =next(file_reader)
        print(headers)

main()
