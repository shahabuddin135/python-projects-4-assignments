# import random


# randomNumber = random.randint(1,10)

# attempts = 0

# while True :
    
#     try:
        
#         userGuess = int(input("enter your guessed number: "))
    
#         if(attempts >= 5):
#                     print("Max attempts reached, Try again!")
#                     break
#         else:
#                 if(userGuess > 10 or userGuess <= 0):
#                     print(f"{userGuess} is not valid, enter number in range of (1 - 10)")
#                     continue
                
#                 elif(userGuess == randomNumber):
#                     print("Correct Guess! 7 crore!")
#                     break
#                 elif(userGuess < randomNumber):
#                     print("low, increase the number")
#                     attempts += 1
#                 elif(userGuess > randomNumber):
#                     print("high, decrease the number")
#                     attempts += 1
#     except:
#         print("invalid user input")    


# in range of starting number and randomNumber

# 8 if the number is in range from random number -1 to starting or end if close to start, too low, if to end too high

# [too low            .  random number    .           too high]
#             close, inc the num    close, dec the num

# if in range of certain number like guess number +2 == randomNumber => too
# close and userguess less than randomNum

# if out of range of certain number like guess number +2 = randomNumber === too far


import random


randomNumber = random.randint(1,10)

attempts = 0

while True :
    
    try:
        
        userGuess = int(input("enter your guessed number: "))
    
        if(attempts >= 5):
                    print("Max attempts reached, Try again!")
                    break
        else:
                if(userGuess > 10 or userGuess <= 0):
                    print(f"{userGuess} is not valid, enter number in range of (1 - 10)")
                    continue
                
                elif(userGuess == randomNumber):
                    print("Correct Guess! 7 crore!")
                    break
                elif(userGuess + 1 < randomNumber):
                    print("too low, increase the number")
                    attempts += 1
                elif(userGuess + 1 == randomNumber):
                    print("too close, increase the number")
                    attempts += 1
                elif(userGuess - 1 > randomNumber):
                    print("too high, decrease the number")
                    attempts += 1
                elif(userGuess - 1 == randomNumber):
                    print("too close, decrease the number")
                    attempts += 1   
                
    except:
        print("invalid user input")    
