import random

random_num = random.randint(1, 10)

def get_user_guess():
    while True:
        try:
            guess = int(input("Guess a number from 1 to 10: "))
            if 1 <= guess <= 10:
                return guess
            print("Please enter a number between 1-10!")
        except ValueError:
            print("Invalid input! Please enter a number.")

def guessing_game():
    while True:
        guess = get_user_guess()
        
        if guess > random_num:
            print("Your guess is too high!")
        elif guess < random_num:
            print("Your guess is too low!")
        else:
            print(f"Correct! The number was {random_num}.")
            break

guessing_game()