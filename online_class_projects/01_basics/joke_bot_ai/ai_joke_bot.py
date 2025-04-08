import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_joke():
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Get user input for additional context
    user_input = input("Enter a prompt for a joke: ").strip()
    
    # Combine role instructions with user input.
    # Note: The role is set to strictly deliver a short joke.
    prompt = (
        "You are a stand-up comedian whose sole purpose is to tell short, concise jokes. "
        "Do not provide any commentary or extra text—only a joke. "
        "Keep your response brief (under 80 tokens). "
        f"User prompt: {user_input}. "
        "Now, deliver your joke."
    )
    
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=80,   # Token limit for a concise response
            temperature=0.95,       # Creative output
            top_p=0.7,
            candidate_count=1
        )
    )
    
    return response.text.strip()

if __name__ == "__main__":
    while True:
        joke = get_joke()
        print("\nJoke:", joke)
        more = input("\nDo you want to hear more jokes? (yes/no): ").strip().lower()
        if more not in ["yes", "y"]:
            print("Okay, goodbye!")
            break
