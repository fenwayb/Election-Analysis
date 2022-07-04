import csv
import os
# Assign a variable for the file to load and save the path

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize variables and lists
total_votes = 0
line = ("-"*24)
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
open(file_to_save, "w")
with open(file_to_load) as election_data:
    #print(election_data)

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print each row in the CSV file.
    # Print the header row.
    headers = next(file_reader)   
    
    for row in file_reader:
        # add to the total vote count
        total_votes += 1  
        candidate_name = row[2]
        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1



# The data we ned to retrieve

# 1. The total numbers of votes cast

#print(total_votes)

# 2. A complete list of candidates who received votes

#print(candidate_options)

# 3. The percentage of votes each candidate won

# Determine the percentage of votes for each candidate by looping through the counts.

# 1. Iterate through the candidate list.

for candidate_name in candidate_votes:

    # 2. Retrieve vote count of a candidate.

    votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of votes.

    vote_percentage = float(votes) / float(total_votes) * 100

    # 4. Print the candidate name and percentage of votes.

    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.\n")

# 4. The total number of Votes each candidate won

#print(candidate_votes)

# 5. The winner of the election based on popular vote

# Determine winning vote count and candidate

# 1. Determine if the votes are greater than the winning count.

    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # 2. If true then set winning_count = votes and winning_percent =

        # vote_percentage.

        winning_count = votes

        winning_percentage = vote_percentage

        # 3. Set the winning_candidate equal to the candidate's name.

        winning_candidate = candidate_name

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (

    f"{line}\n"

    f"Winner: {winning_candidate}\n"
    
    f"Winning Vote Count: {winning_count:,}\n"
    
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    
    f"{line}\n")
print(winning_candidate_summary)

# Close the file.
election_data.close()

# Use the open statement to open the file as a text file.
# Using the with statement open the file as a text file.

with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
      txt_file.write(f"Counties in the Election\n{line}\n")
      txt_file.write("Arapahoe\nDenver\nJefferson")

