import random
from hangman_art import hangman


def choose_word():
    with open("wordbank.txt", "r" ) as file:
        words = file.read().splitlines()
    return random.choice(words)

def play_game():
    
   word_to_guess = choose_word()
   
   display = ["_"] * len(word_to_guess)
   lives = 6
   guess_letters = []
   hangman
   
   while "_" in display and lives > 0:
       
        print(f"\n{' '.join(display)}")
        print(f"Lives left: {lives}")
        print(hangman[lives])
        
        guess  = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter a single letter.")
            continue
       
        if guess in guess_letters:
            print(f'You already guessed "{guess}" ')
            continue
        guess_letters.append(guess)
        
        if guess in word_to_guess:
            
            display = [guess if word_to_guess[i] == guess else display[i] for i in range(len(word_to_guess))]
        else:
            lives -= 1
            print(f"❌ '{guess}' is not in the word.")
            
   if "_" not in display:
        print(f"\n{' '.join(display)}") 
        print("You won!")
   else:
        print(hangman[0])
        print(f"💀 Game over! The word was: {word_to_guess}")

play_game()