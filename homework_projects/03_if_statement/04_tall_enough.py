
def tall_enough():
    
    allowed_height = 5.5
    
    while True:
        user_input = input("Enter your height (press 'enter' to exit): ")
        
        if user_input == "":
            print("\nExiting the program. Goodbye!")
            return         
        try:
           height = float(user_input)
        except ValueError:
                
                print("Invalid year input, enter a number")
                return
        
        if height >= allowed_height:
            print("You can ride the roller coaster.")
        else:
            print("You cannot ride the roller coaster.")

tall_enough()