import random
import inquirer

def play_game():
    
    while True:
        
        question = [
            inquirer.List(
            "choice",
            message="Choose from Rock, Paper and Scissors",
            choices=["rock","paper","scissors"]
            )
        ]
    
        answer = inquirer.prompt(question)
        
        user_choice = answer["choice"]
        
        choices = ("rock","paper","scissors")
        computer_choice = random.choice(choices)
        print(f"computer choice: {computer_choice}")
        
        if(user_choice == computer_choice):
            print("tie")
            continue
        
        elif(
            
            (user_choice == "rock" and computer_choice == "scissors" ) or
            (user_choice == "paper" and computer_choice == "rock" ) or
            (user_choice == "scissors" and computer_choice == "paper" )
            
            ):
            print("You Won 🎉")
            
        else:
            print("you lose, Better luck next time")
        
        replay = input("\nDo you want to play again? (y/n): ").strip().lower()
        if replay != "y":
               
           print("Thanks for playing! Goodbye.")
           break
        
play_game()
