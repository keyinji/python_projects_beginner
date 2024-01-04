import random

dice = [1, 2, 3, 4, 5, 6]

def main():
    while True:
        user_input = input("Press enter to roll the dice or type 'quit' to exit: ")
        if user_input.lower() == "quit":
            break
        else:
            choice = random.choice(dice)
            print(f"You rolled {choice}")

if __name__ == "__main__":
    main()
    
