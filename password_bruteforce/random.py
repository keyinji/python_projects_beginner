import itertools
import time

# Define all characters to use in the password
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Define the password to be cracked
password = "password"

# Define the maximum password length to try
max_length = 8

# Track the start time of the password cracking process
start_time = time.time()

# Try all possible combinations of characters with a length of 8
for combination in itertools.product(chars, repeat=max_length):
    # Join the characters in the combination to form a password candidate
    candidate = "".join(combination)
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
