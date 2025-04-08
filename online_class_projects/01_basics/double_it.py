
def double(num):
    while num < 100:
        num *= 2  
        
    return num

user_number = int(input("Enter a number to double it: "))
print(double(user_number))
