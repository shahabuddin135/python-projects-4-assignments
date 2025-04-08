
def triple_it():
    user_input = input("Enter your input: ")
    arr = []
    print(f"Initial list: {arr}")
    for _ in range(3):
        arr.append(user_input)
    
    print(f"Final list: {arr}")
    
    return arr

triple_it()

