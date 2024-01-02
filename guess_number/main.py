

# Import the random module
import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Get the user's guess
guess = int(input("Guess a number between 1 and 100: "))

# Check if the user's guess is correct
while guess != number:
    if guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess = int(input("Guess again: "))

# Print a message to the user if they guessed correctly
print("Congratulations! You guessed the correct number.")