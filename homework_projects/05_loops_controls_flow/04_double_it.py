
def double(num):
    while num < 100:
        num *= 2  
        print(num)
        
    return num

# user_number = int(input("Enter a number to double it: "))
# print(double(user_number))



#2nd appraoch

#what if we do not want the number to exceed the 100
#this logic returns the final output but behind the scene it still exceeds 100 (not good)

def double_it(num):
    while num < 100:
        num *= 2  
        print(num)
        if num > 100:
            num //= 2 # or num -= num // 2
            print(f"Less than 100: {num}")
            break
        
    return num

user_number = int(input("Enter a number to double it: "))
double_it(user_number)


# third approach

def double():
    """
    Continuously doubles a user-provided number while ensuring the result never exceeds 100.
    Prints each valid doubled value and stops before any operation that would exceed the limit.

    API Call Cost Scenario Explanation:
    - Imagine doubling `num` is an API call costing $100 per operation.
    - The condition `while num * 2 < 100` acts as a pre-check to ensure the API call (doubling) 
      will NOT exceed 100 **before** executing it. This avoids any cost for invalid operations.
    - The doubling operation (`num *= 2`) is only performed if the pre-check passes, ensuring 
      no value ever exceeds 100.

    Example:
      Input: 2 → Output: 4, 8, 16, 32, 64 (stops before 128)
      Input: 50 → Output: 100 is skipped (50*2=100 → loop condition fails).

    Notes:
      - The initial input is not validated (e.g., entering 100 directly will print nothing).
      - All operations are strictly safe: no doubled value ever reaches or exceeds 100.
    """
    num = float(input("Enter a number to double: "))
  
    while num * 2 < 100:  # PREDICT safety of next operation
        num *= 2  # "API call" only happens if safe
        print(f"Doubled: {num}")
      

double()