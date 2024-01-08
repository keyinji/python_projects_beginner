import random

words = [
    "mystery", "quizzical", "jazz", "buzzing", "fizz", "haphazard",
    "zigzagging", "fluffy", "puzzle", "jinx", "gazebo", "kiwifruit",
    "oxygen", "vodka", "whiskey", "symphony", "zodiac", "voyage",
    "wizard", "yacht"
]

def opportunities(chances):
    if chances == 6:
        print("6 tries remaining")
    elif chances == 5:
        print("5 tries remaining")
    elif chances == 4:
        print("4 tries remaining")
    elif chances == 3:
        print("3 tries remaining")
    elif chances == 2:
        print("2 tries remaining")
    elif chances == 1:
        print("1 try remaining")
    else:
        print("You lost")

def hangman():
    word = random.choice(words)  # Randomly choose a word from the list
    guessed = "_" * len(word)  # Create a string of underscores same length as word
    guessed_correctly = set(word)  # Unique characters in the word
    guessed_letters = set()  # What letters have been guessed
    chances = 6

    print("Welcome to Hangman!")
    print(guessed)  # Show the initial word as underscores

    while len(guessed_correctly) > 0 and chances > 0:
        guess = input("Guess a letter: ").lower()
        
        # Check if the guessed letter is in the word
        if guess in guessed_correctly:
            guessed_correctly.remove(guess)
            print("Correct!")
            
            # Reveal the guessed letter in the word
            guessed = ''.join([letter if letter in guessed_letters or letter == guess else "_" for letter in word])
            guessed_letters.add(guess)
        else:
            if guess not in guessed_letters:
                chances -= 1
                opportunities(chances)
                guessed_letters.add(guess)
            else:
                print("You already guessed that letter")
        
        print(guessed)

    if chances == 0:
        print(f"You lost! The word was {word}.")
    else:
        print("Congratulations! You guessed the word!")

# Run the game
hangman()


    
