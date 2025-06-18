# welcome message
# user choose their difficulty(easy , normal , hard)
# easy 10 chance , medium 5 chance , hard 3 chances
# prompt for great you have selected the ... difficulty level.
# computer picks a random number between 1-100
# user guess the number
# count how many guesses that they have made to get it right
# give clues to users if the nymber is greater or less

import random

def pick_number():
    return random.randint(1,100)

number = pick_number()

def main():
    welcome_message()
    choice = choose_difficulty()

    if choice == 1:
        print("Great! You have selected the Easy difficulty level.")
        print("Let's start the game!")
        easy_mode(number)

    if choice == 2:
        print("Great! You have selected the Normal difficulty level.")
        print("Let's start the game!")
        normal_mode(number)

    if choice == 3:
        print("Great! You have selected the Hard difficulty level.")
        print("Let's start the game!")
        hard_mode(number)

def welcome_message():
    print("\nWelcome To Guess The Number!")
    print("I'm thinking of a number between 1 and 100")
    print("You have multiple chances based on the difficulty you choose.")

def choose_difficulty():
    print("Please select the difficulty level:")
    print("\n1. Easy (10 chances)")
    print("2. Normal (5 chances)")
    print("3. Hard (3 chances)")

    return int(input("Enter your choice: "))

def easy_mode(num):
    try:
        chance = 10
        count = 1
        while True:
            if chance <= 0:
                print("Better luck next time!")
            
            user_guess = int(input("Please guess the number: "))
            
            if user_guess > num:
                print(f"{user_guess} is greater than the number")
                chance -= 1
                count += 1
            elif user_guess < num:
                print(f"{user_guess} is less than the number")
                chance -= 1
                count += 1
            elif user_guess == num:
                print(f"Congratulations! You guessed the number in {count} attempts")

    except ValueError:
        print("Please enter a number")

def normal_mode(num):
    try:
        chance = 5
        count = 1

        while True:
            if chance <= 0:
                print("Better luck next time!")

            user_guess = int(input("Please guess the number: "))

            if user_guess > num:
                print(f"{user_guess} is greater than the number")
                chance -= 1
                count += 1
            elif user_guess < num:
                print(f"{user_guess} is less than the number")
                chance -= 1
                count += 1
            elif user_guess == num:
                print(f"Congratulations! You guessed the number in {count} attempts")
    except ValueError:
        print("Please enter a number")

def hard_mode(num):
    try:
        chance = 3
        count = 1

        while True:
            if chance <= 0:
                print("Better luck next time!")

            user_guess = int(input("Please guess the number: "))

            if user_guess > num:
                print(f"{user_guess} is greater than the number")
                chance -= 1
                count += 1
            elif user_guess < num:
                print(f"{user_guess} is less than the number")
                chance -= 1
                count += 1
            elif user_guess == num:
                print(f"Congratulations! You guessed the number in {count} attempts")
    except ValueError:
        print("Please enter a number")


if __name__ == "__main__":
    main()
            
            






        

    
    



