import os
import google.generativeai as genai
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set it in the .env file.")

genai.configure(api_key=api_key)

# Generate a Random Game Scenario
def generate_game_scenario():
    themes = [
        "a haunted mansion full of ghosts",
        "a futuristic cyberpunk city with hackers and AI",
        "a medieval kingdom under siege",
        "a stranded spaceship lost in deep space",
        "a detective mystery in a noir-style city",
        "a pirate adventure on the high seas"
    ]
    theme = random.choice(themes)
    prompt = f"Create an interactive text-based game where the player explores {theme}. Start with an engaging introduction and an opening choice for the player."
    
    response = genai.generate_content(prompt=prompt)
    
    return response.result if response else "No response from AI."

# Define the AI Chat Function for Interactive Gameplay
def chat_with_ai(prompt, story_history):
    try:
        formatted_history = "\n".join([f"{turn['role'].upper()}: {turn['content']}" for turn in story_history])
        prompt_with_history = f"{formatted_history}\nUSER: {prompt}"
        
        response = genai.generate_content(prompt=prompt_with_history)
        
        return response.result if response else "No response from AI."
    except Exception as e:
        return f"An error occurred: {e}"

# Main Game Loop
def main():
    print("Welcome to the AI-driven text-based adventure game! Type 'quit' to exit.")
    story_history = []
    
    # Start with a randomly generated game scenario
    game_intro = generate_game_scenario()
    print("\n" + game_intro)
    story_history.append({"role": "assistant", "content": game_intro})
    
    while True:
        player_input = input("\nWhat do you do? ")
        if player_input.lower() == "quit":
            print("Thanks for playing! Goodbye.")
            break

        story_history.append({"role": "user", "content": player_input})
        ai_response = chat_with_ai(player_input, story_history)

        print("\n" + ai_response)

        story_history.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    main()
