 #Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: CInitialize a county list, like the candidate_options list, that will hold the names of the counties
# Initialize a dictionary, like the candidate_votes dictionary, that will hold the county as the key and the votes cast for each county as the values.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_county = 0
winning_percentage = 0
winning_c_percentage = 0

# 2: Initialize an empty string, like winning_candidate that will hold the county name for the county with the largest turnout.
#Initialize a variable, like the winning_cute variable, that will hold the number of votes of the county that had the largest turnout.
lrg_turnout_county = ""
lrg_turn_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name and county name from rows.
        candidate_name = row[2]

        # 3: While reading the election results from each row inside the for loop, write a script that gets the county name from each row.
        county_name = row[1]


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write a decision statement with a logical operator to check if the county name acquired in Step 3 is in the county list you created in Step 1.
        if county_name not in county_options:  

            # 4b: If the county is not in the list created in Step 1, add it to the list of county names like you did when adding a candidate to the candidate_options list
            county_options.append(county_name)

            # 4c: Write a script that initializes the county vote to zero, like you did when you began to track the vote counts for the candidates.
            county_votes[county_name] = 0

        # 5: Write a script that adds a vote to the county’s vote count as you are looping through all the rows, like you did for the candidate’s vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n-------------------------\n"
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a repetition statement to get the county from the county dictionary that was created in Step 1.
    for county_name in county_votes:
        # 6b: Initialize a variable to hold the county’s votes as they are retrieved from the county votes dictionary.
        county = county_votes.get(county_name)

        # 6c: Write a script that calculates the county’s votes as a percentage of the total votes.
        county_percentage = float(county) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {county_percentage:.1f}% ({county:,})\n")

         # 6d:Write a print statement that prints the current county, its percentage of the total votes, and its total votes to the command line.
        print(county_results, end="")
         # 6e: Write a script that saves each county, the county’s total votes, and the county’s percentage of total votes to the election_results.txt file.Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f:Write a decision statement that determines the county with the largest vote count and then adds that county and its vote count to the variables created in Step 2.
        if (county > winning_county) and (county_percentage > winning_c_percentage):
            winning_county = county
            winning_c_candidate = county_name
            winning_c_percentage = county_percentage

    #7:Write a print statement that prints out the county with the largest turnout.After you run your solution to Deliverable 1, confirm that the output to the command line matches the following image:
    winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_c_candidate}\n"
        f"Winning County Vote: {winning_county:,}\n"
        f"Winning County Percentage: {winning_c_percentage:.1f}%\n"
        f"-------------------------\n\n"
        f"Candidate Percentage of Votes:\n"
        f"-------------------------\n")
    print(winning_county_summary)

    # 8: Write a script that saves the county with the largest turnout to the election_results.txt file.
#After you run your solution to Deliverable 2, confirm that your election_results.txt file matches the following image:Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"\n-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)