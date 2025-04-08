import time

#approach one

def liftoff(countdown_time):
    
    while countdown_time >= 0:
        
        mins,secs = divmod(countdown_time,60)
        
        print(f"Time remaining to lift off: {mins:02d}:{secs:02d}", end="\r", flush=True)
        
        if countdown_time == 0:
            print("\nLift off! GO Starship Go 🚀")  
            break
        time.sleep(1) 
        countdown_time -= 1
    

try:
    initial_time = int(input("Enter time to liftoff (in seconds) 🚀: "))
    liftoff(initial_time)
except ValueError:
    print("Please enter a valid number!")
        

#approach 2

# count_down = 11

# while count_down >= 0:
     
#      time.sleep(1)
#      count_down -=1
#      print(f'countdown: {count_down:2d}', end='\r')
     
#      if count_down == 0:
#          print("\nLift Off Go Go Go!")
#          break


