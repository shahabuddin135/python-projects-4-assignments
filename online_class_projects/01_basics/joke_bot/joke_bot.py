# from inputs import stored_inputs
from jokes import jokes
import random
from textblob import TextBlob #for auto spelling correction (spell bee winner #1)

# stored_inputs = [s.lower().strip() for s in stored_inputs] # removing white space and turning to lowercase

def tell_joke():
    
    user_input = TextBlob(input("what do you want?")).correct().strip().lower()
    
    if ("joke" in user_input):
        print(random.choice(jokes))
    else:
        print("I don't understant")

if __name__ == "__main__":
    tell_joke()