# take user input, name and contact, validate them both and create a key if not exist in the dictionary, assign it 



def phone_book():
    
    phone_book = {}
    
    while True:
        
            user_name = input("Enter contact name (or press Enter to stop): ").strip()

            if user_name == "":
                break
            
            user_number = input("Enter contact number: ").strip()
            
            if user_number == "":
                print("Number cannot be empty")
                continue
            
            if not user_number.isdigit():
                print("Invalid input, enter a number.\n")   
                continue
                    
            if user_number in phone_book: 
            
                print(f"{user_number} already saved! Updating number...")
            
            phone_book[user_name] = user_number
                
    if not phone_book:
        print("No contacts availible")
    else:
        print(f"Saved {'contact' if len(phone_book) ==1 else 'contacts'}:")
    
        for name,number in phone_book.items():
            print(f"{name} -> {number}")   
         

phone_book()