def count_occurance():
    
    num_dict = {}
    while True:
        user_input = input("Enter a number to count (or 'exit' to stop): ").strip()
        
        if user_input == "exit" or user_input == "":
            break        
        try:
            num = int(user_input)
            
            if num not in num_dict:
                num_dict[num] = []
            num_dict[num].append(num)
        except ValueError:
            print(print("Invalid input! Please enter a number."))
            
    for key,value in num_dict.items():
        print(f"{key} appeared {len(value)} {'time' if len(value) == 1 else 'times'}")
    

count_occurance()

"""
    Continuously prompts the user to enter numbers and counts the number of times each number is entered.

    - The user is prompted to input a number repeatedly.
    - If the user types 'exit' or presses Enter without typing anything, the loop ends.
    - For each valid integer input, the number is added to a dictionary and its occurrences are tracked.
    - If the input is not a valid integer, an error message is shown.
    - After exiting the loop, the function prints how many times each number was entered.

    Example:
        Enter a number to count (or 'exit' to stop): 5
        Enter a number to count (or 'exit' to stop): 3
        Enter a number to count (or 'exit' to stop): 5
        Enter a number to count (or 'exit' to stop): exit
        Output:
        5 appeared 2 times
        3 appeared 1 time
"""