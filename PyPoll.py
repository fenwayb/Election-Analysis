import csv
import os
# Assign a variable for the file to load and the path

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
open(file_to_save, "w")
with open(file_to_load) as election_data:
    #print(election_data)


# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print each row in the CSV file.
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
    #for row in file_reader:
        #print(row)  

# Close the file.
election_data.close()

# The data we ned to retrieve
# 1. The total numbers of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of Votes each candidate won
# 5. The winner of the election based on popular vote

# Use the open statement to open the file as a text file.
# Using the with statement open the file as a text file.

line = ("-"*24)
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
      txt_file.write(f"Counties in the Election\n{line}\n")
      txt_file.write("Arapahoe\nDenver\nJefferson")

