
# def leap_or_not():
    
#     try:
#         year = int(input("Enter a year to find out if it's a leap year: "))
    
#     except ValueError:
#         print("Invalid year input, enter a number")
#         return
        
#     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        
#         print(f"{year} is a leap year!")
#     else:
#         print(f"{year} is not a leap year!")

# leap_or_not()


#2nd code for logic 

# prints the list ranges of leap years and normal years

def leap_or_not():
    
    try:
        from_year = int(input("Enter a initial year to find out if it's a leap year: "))
        to_year = int(input("Enter a year to find out if it's a leap year: "))
    
    except ValueError:
        print("Invalid year input, enter a number")
        return
    
    leap_years = []
    normal_years = []
    
    for year in range(from_year,to_year):
         
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            leap_years.append(year)   
        else:
            normal_years.append(year)

    print(f"Leap years: {leap_years}")
    print(f"Normal years: {normal_years}")
    
leap_or_not()
