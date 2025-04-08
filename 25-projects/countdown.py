import time
import winsound

def get_seconds():
    while True:
        try:
            seconds = int(input("Enter seconds to start coundown: "))
            
            if seconds >= 0 :
                return seconds
            else:
                print("Enter number above 0")
        except ValueError:
            print("Invalid input. Enter a number.")

total_time = get_seconds()


while total_time >= 0:
    
    min,sec = divmod(total_time,60)
    print('Time remaining:' + " " + '{:02d}:{:02d}'.format(min,sec), end="\r" ,)
    time.sleep(1)
    total_time -=1
    # winsound.Beep(4000, 150)
    # time.sleep(0.001) 
    # winsound.Beep(4000, 150)
    winsound.Beep(3000, 100)
    time.sleep(0.0001)
    winsound.Beep(3000, 100)

print("\nTIME IS UP!")
    
    