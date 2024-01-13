
import string
import random

# Ask for the number of characters in the password
num_characters = input("How many characters do you want in your password? ")

# Create a string of all possible characters
all_characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random password
password = ''.join(random.choice(all_characters) for i in range(int(num_characters)))

# Print the password
print(password)


