import itertools
import time

# Define all characters to use in the password
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Define the password to be cracked
password = "20071231"

# Define the maximum password length to try
max_length = 2  # Reduced max_length to account for the known characters

# Define the possible fourth characters
fourth_chars = ['6', '7']

# Define the possible values for fifth and sixth characters (01-12)
fifth_sixth_chars = ['{:02d}'.format(i) for i in range(1, 13)]

# Define the possible values for seventh and eighth characters (01-31)
seventh_eighth_chars = ['{:02d}'.format(i) for i in range(1, 32)]

# Track the start time of the password cracking process
start_time = time.time()

# Try all possible combinations of characters for the remaining characters
for fourth_char in fourth_chars:
    for fifth_sixth_char in fifth_sixth_chars:
        for seventh_eighth_char in seventh_eighth_chars:
            candidate = "200" + fourth_char + fifth_sixth_char + seventh_eighth_char
            print("Trying password:", candidate)
            # Check if the candidate matches the password
            if candidate == password:
                # Track the end time of the password cracking process
                end_time = time.time()
                print("Password found:", candidate)
                # Calculate the time taken to crack the password
                time_taken = end_time - start_time
                print("Time taken:", time_taken, "seconds")
                # Terminate the password cracking process
                raise SystemExit