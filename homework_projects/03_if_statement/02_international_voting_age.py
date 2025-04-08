 
countries_voting_age = {
    
    "abistan":18,
    "beebistan":20,
    "ceebistan":25,
    "deebistan":36
}


def voting_age_comparision():
  
    try:  
        user_age = int(input("Enter your age: "))
    except ValueError:    
            print("Invalid age input, enter a number")
            return
    allowed = []
    not_allowed = []
    
    for country, age in countries_voting_age.items():
        
        if user_age < age:
            
            not_allowed.append(country)
        else:    
            allowed.append(country)

    if allowed:
        print(f"You can vote in: {allowed}")
        
    if not_allowed:
        print(f"You cannot vote in: {not_allowed}")
    
voting_age_comparision()

# G, i am thinking
# #loop over the disctionalry and get the country age, 
# # and match it with the user input, and return the other countries ages
# # too stating that you are not allowed to vote or allowed to votre in these countries


# # if number is greator or equal to the country voting age, you can vote!!

