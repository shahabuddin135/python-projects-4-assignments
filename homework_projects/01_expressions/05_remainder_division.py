
def get_remainder_quotient():
    num1 = int(input("Please enter an integer to be divided: "))
    num2 = int(input("Please enter an integer to divided by: "))
    
    # quotient =  num1 // num2
    # remainder = num1 % num2
    
    quotient , remainder = divmod(num1,num2)
    
    return {
        "quotient":quotient,
        "remainder":remainder
    }
    
# get_remainder_quotient()

result1 = get_remainder_quotient()

print(result1) 