import random
from textblob import TextBlob

fruit_prices = {
    "apple": 10,
    "banana": 23,
    "mango": 34,
    "orange": 76,
    "cherry": 5,
    "grape": 45,
    "pineapple": 120,
    "strawberry": 150,
    "watermelon": 80,
    "blueberry": 200,
    "pear": 30,
    "kiwi": 60,
    "peach": 40,
    "plum": 25,
    "pomegranate": 90,
    "fig": 55,
    "guava": 35,
    "apricot": 70,
    "blackberry": 180,
    "raspberry": 170
}

def fruit_price_teller():
    """
    A simple fruit price calculator.

    Prompts the user to enter fruit names, auto-corrects spelling if needed,
    displays the fruit price, adds it to the total, and shows the final bill.
    If a fruit is not found, assigns a random price.
    """
    
    total = 0
    
    while True:
        user_input = input("Enter a fruit name (press enter or write 'exit' to quit): ").strip().lower()
        
        corrected_fruit = str(TextBlob(user_input).correct())
        
        if corrected_fruit != user_input:
            print(f"Did you mean to write '{corrected_fruit}'? (y/n)")
            choice = input().strip().lower()
            if choice == "y":
                fruit_name = corrected_fruit
            else:
                fruit_name = user_input
        else:
            fruit_name = user_input
        
        if fruit_name == "" or fruit_name == "exit":
            break
        
        if fruit_name not in fruit_prices:
            fruit_prices[fruit_name] = random.randint(10, 100)
        
        print(f"The price of {fruit_name} is ${fruit_prices[fruit_name]}.")
        total += fruit_prices[fruit_name]
        
    print(f"\nYour total is: ${total}")
    return total


fruit_price_teller()
