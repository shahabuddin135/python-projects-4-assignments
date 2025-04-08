

def play_game():
        
    attempts = 0

    low = 1
    high = 100

    while low <= high:
        
        guess = (low + high) // 2
        attempts += 1
        
        userFeedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        feedbackRule:tuple = ("h","l","c")
        if userFeedback not in feedbackRule:
            print("invalid feedback, enter from the given keywords: (h , l , c)")
            continue  # Ask again without counting this as an attempt
        else:
            
            
                if (userFeedback == "c"):
                    print(f"🎉 I guessed it in {attempts} attempts!")
                    break
                elif(userFeedback == "h"):
                    high = guess - 1
                elif(userFeedback == "l"):
                    low = guess + 1
            
                if attempts >=5:
                    print("Max attempts reached! try again")
                    break
    
    replay = input("\nDo you want to play again? (y/n): ").strip().lower()
    if replay == "y":
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

                    
play_game()