def get_first_element():
    
    arr = []
    
    while True:
        user_input = input("Enter any number of items you want, (to stop press enter)': ")
        
        if not user_input:
            break
        arr.append(user_input)

    print(f"Full list: {arr} ")
    return arr[-1] if arr else None

result = get_first_element()
print("Last element: ", result) 