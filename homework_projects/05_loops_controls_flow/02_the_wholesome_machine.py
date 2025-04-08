import random
import time
from textblob import TextBlob
from colorama import Fore, init
init(autoreset=True)


#affirmations
affirmations = [
    "I am capable of achieving greatness.",
    "My potential is limitless.",
    "Challenges are opportunities for growth.",
    "I am resilient, and I bounce back from setbacks.",
    "I am in control of my destiny and make choices that lead to success.",
    "I believe in myself and my abilities.",
    "I am worthy of happiness and fulfillment.",
    "Every day, I become a better version of myself.",
    "I have the power to create positive change in my life.",
    "I am surrounded by love and support.",
    "I trust the journey and embrace the process of growth.",
    "I am confident in my decisions and actions.",
    "I radiate positivity and attract good things into my life.",
    "I am grateful for the opportunities that come my way.",
    "I am dedicated to achieving my goals and dreams.",
    "I have the strength to overcome any obstacle.",
    "I am proud of my accomplishments and celebrate my successes.",
    "I am constantly learning and evolving.",
    "I am deserving of all the good things life has to offer.",
    "I am at peace with who I am and who I am becoming."
]

#Encouraging Dialogs that make the user affirm

encouragement_dialogues = [
    "Taking a moment to write down your thoughts can be a powerful tool for self-reflection. Why not jot down an affirmation that resonates with you?",
    "Your words have the power to shape your mindset. How about crafting an affirmation to inspire your day?",
    "Reflecting on positive statements can uplift your spirit. Would you like to write an affirmation to reinforce your goals?",
    "Let's channel some positivity! Penning down an affirmation can set a constructive tone for your endeavors.",
    "Affirmations can be a beacon during challenging times. Care to write one that aligns with your aspirations?",
    "Empower yourself by articulating your strengths. How about noting down an affirmation that highlights your capabilities?",
    "Writing affirmations can be a step towards personal growth. What positive statement would you like to affirm today?",
    "Your journey is unique and valuable. Capture its essence by writing an affirmation that speaks to your path.",
    "Harness the power of positive thinking. Drafting an affirmation can be a great start to cultivating a resilient mindset.",
    "Self-affirmation is a form of self-care. Take a moment to write a statement that celebrates you."
]

#dialogs after the user affirms

affirmation_responses = [
    "That's a wonderful affirmation! Keep believing in yourself.",
    "Your words have power. That affirmation is truly inspiring.",
    "Fantastic! Repeating this affirmation daily can make a big difference.",
    "I appreciate your positive affirmation. It's uplifting!",
    "Great job! Affirmations like this can boost your confidence.",
    "Such a powerful statement. Keep up the positive self-talk!",
    "Your affirmation reflects a strong and positive mindset.",
    "Impressive! That affirmation can lead to meaningful change.",
    "Well said! Embracing this affirmation can enhance your well-being.",
    "Excellent! Keep nurturing yourself with such affirmations."
]

#failed affirmations

refusal_responses = [
    # Harsh responses
    "Neglecting self-affirmation is a choice to remain stagnant. Is that what you want?",
    "By refusing to affirm yourself, you're actively choosing self-doubt over self-belief.",
    "Skipping affirmations again? Perhaps complacency is more comfortable than growth.",
    "If you can't take a moment for self-affirmation, maybe you're not ready for progress.",
    "Avoiding affirmations is like rejecting your own potential. Think about that.",

    # Humorous responses
    "No affirmations today? Even superheroes give themselves pep talks, you know!",
    "Skipping affirmations? Your future self just sent a disapproving emoji.",
    "No time for affirmations? Guess we'll postpone greatness to another day!",
    "Avoiding affirmations is like a plant avoiding sunlight. Photosynthesis, anyone?",
    "Skipping affirmations? Hope you enjoy the company of your comfort zone!",

    # Regret-inducing reminders
    "Every day without self-affirmation is a missed opportunity for growth. Don't let today be one.",
    "Neglecting affirmations now might lead to wondering 'what if' later. Choose wisely.",
    "Skipping this could be a small step towards a future regret. Is it worth it?",
    "Imagine looking back and realizing that consistent affirmations were the key you ignored.",
    "Today's choices shape tomorrow's reality. Avoiding affirmations might shape a future you'd rather not face."
]


def wholesomeMachine():
    
    affirmation = random.choice(affirmations).strip().lower()
    encouragement = random.choice(encouragement_dialogues)
    affirmed = random.choice(affirmation_responses)
    failed_affirm = random.choice(refusal_responses)
    
    while True:
        affirmation = random.choice(affirmations).strip().lower()
        encouragement = random.choice(encouragement_dialogues)
        affirmed = random.choice(affirmation_responses)
        failed_affirm = random.choice(refusal_responses)
    
        print(Fore.BLUE + f"\n{encouragement}: ")
        time.sleep(1)
        print(Fore.GREEN + f"\nAffirmation: \"{affirmation}\"")
        time.sleep(1)
        
        raw_input = input(Fore.YELLOW + f"\nWrite here: ")
        
        origional_words = raw_input.split()
        
        corrected = str(TextBlob(raw_input).correct()).strip().lower()
        corrected_words = corrected.split()
        
        if origional_words != corrected_words:
            print(Fore.LIGHTBLACK_EX + "\nCorrections made:")
            for orig,corr in zip(origional_words,corrected_words):
                if orig != corr:
                    print(Fore.LIGHTBLACK_EX + f" '{orig}' => '{corr}' ")
            time.sleep(1)
        
        if not corrected.endswith("."):
           corrected = corrected + "."
        
        
        if corrected == affirmation:
            print(Fore.MAGENTA + f"\n{affirmed}")
            break
        else:
            print(Fore.RED + f"\n{failed_affirm}")
            continue

wholesomeMachine()
