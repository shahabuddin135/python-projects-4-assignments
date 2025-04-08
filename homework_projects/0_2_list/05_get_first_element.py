
# def get_first_element():
    
#     arr = []
    
#     while True:
#         user_input = input("Enter any number of items you want, (to stop press enter)': ")
        
#         if user_input.lower() == "s":
#             break
#         else:
#             arr.append(user_input)
#             user_input
#     print(f"Full list: {arr} ")
#     return arr[0]

# result = get_first_element()
# print(result)



#2nd approach



def get_first_element():
    
    arr = []
    
    while True:
        user_input = input("Enter any number of items you want, (to stop press enter)': ")
        
        if not user_input:
            break
        arr.append(user_input)

    print(f"Full list: {arr} ")
    return arr[0] if arr else None

result = get_first_element()
print("First element:", result) 

#G! im listening continue and if statements use modulo hmmm phir use parameter
# pass and argument into a funcion that parameter will be used as range (is it the answer?).........
#let me see your screen

