# V1

# import random

# random_range = random.randint(1,100)

# for num in range(1,10):   #prints a number number ninetimes which is generated randomly at the beginning
    
#     print(random_range)
    

#V2
    
# import random

# ones = ["one","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]

# for num in range(10):
    
#     print(f"{ones[num]}: {random.randint(1,100)}") #prints 10 random numbers each time because the random.randit runs 10 different times
 
 
#V3 on steroids ++ 

import random

ones = ["", "One", "Two", "Three","Four", "Five","Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve","Thirteen", "Fourteen","Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "", "Twenty", "Thirty", "Forty","Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

def num_to_words(num):
        if num == 0:
            return "zero"
        elif 1 <= num <= 9:
          return  ones[num]
        elif 10 <= num <= 19:
          return  teens[num - 10]
        elif 20 <= num <= 99:
           ten_part = tens[num // 10]
           one_part = ones[num % 10]
           return f"{ten_part} {one_part}".strip() if one_part else ten_part
        else:
            return str(f'Out of range number, cannot covert: {num}')    
        
for _ in range(10):
    rand_num = random.randint(0, 99)
    print(f"{rand_num:2d}: {num_to_words(rand_num)}")  

#output

# 58: Fifty Eight
#  4: Four
# 77: Seventy Seven
#  4: Four
# 37: Thirty Seven 
# 80: Eighty       
# 88: Eighty Eight 
# 40: Forty        
# 47: Forty Seven
# 37: Thirty Seven


   
#V3 on Steroids LOGIC TRIAL & ERROR

#seperate functions for conversion but chose to simplify using if else

# def ones_w(num):
#     if 0 > num <= 9:
#         return ones[num]


# def teens_w(num):
#     if 10 >= num <= 19:
#         return teens[num]

# def tens_w(num):
#     if 10 >= num < 100:
#         return tens[num] // 10 + " " + ones(num % 10)
