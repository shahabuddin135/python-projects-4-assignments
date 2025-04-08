#for even

def print_even(range_limit):
    evens = []
    num = 0  
    for _ in range(range_limit):
        # print(num)
        num += 2  
        evens.append(num)
    print(f"Even numbers: {evens}")
    return evens
# print_even(20)        

#for odd


def print_odd(range_limit):
    
    odds = []
    num = 1
    for _ in range(range_limit):
        # print(odd)
        num +=2
        odds.append(num)
    print(f"Odd numbers: {odds}")
    return odds
# print_odd(20)        


#Get both odd even 

def get_odd_even():
    
    try:
        user_selection = input("Enter O/o for odd numbers or E/e for even numbers: ").strip().lower()
        
        if user_selection not in ["o","e"]:
            print("invalid input only o/O or E/e is valid")
            return
        
        user_range = int(input(f"Enter the range of {user_selection}{"dd" if user_selection == "o" else "ven"} numbers: "))
        
        if(user_selection == "o"):
            print_odd(user_range)
        
        else:
            print_even(user_range)
    
    except ValueError:
        
        print("Thank for using odd even program")
        
    
get_odd_even()    

#well this was heck a lot of work, but i enjoy coding, bye!