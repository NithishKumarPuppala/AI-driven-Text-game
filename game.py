import os
import random
from dotenv import load_dotenv
import cohere

# Loads environment variables from a .env file. This is where we'll store the API key.
# Create a .env file in your project root and add your Cohere API key like this:
# COHERE_API_KEY="YOUR_API_KEY"
load_dotenv()

# --- Configuration ---
# Get the API key from the environment variables.
api_key = os.getenv("COHERE_API_KEY")
if not api_key:
    # If the key isn't found, we stop the script with an error.
    raise ValueError("Cohere API key not found. Please set it in your .env file.")

# Initialize the Cohere client with our API key. This object is our gateway to the API.
co = cohere.Client(api_key)
MODEL_NAME = "command-r"  # We'll use the command-r model, it's great for creative tasks.

# --- Core Game Functions ---

def generate_game_scenario():
    """Kicks off the game by generating a random scenario using the Cohere API."""
    themes = [
        "a haunted mansion full of ghosts",
        "a futuristic cyberpunk city with hackers and AI",
        "a medieval kingdom under siege",
        "a stranded spaceship lost in deep space",
        "a detective mystery in a noir-style city",
        "a pirate adventure on the high seas"
    ]
    # Pick a random theme to keep things interesting.
    theme = random.choice(themes)
    
    # We'll craft a detailed prompt for the AI. It's important to be specific about the desired format
    # to get a clean response that looks like a game.
    prompt = (
        f"You are a text-based adventure game. Create an interactive story where the player explores {theme}. "
        "Start with an engaging introduction paragraph that sets the scene. "
        "Then, on a new line, provide 2-3 numbered choices for the player's first action. "
        "Only output the introduction and the choices. Do not include any other text or explanation."
    )

    try:
        # Make the first call to Cohere to get our starting scene.
        response = co.chat(
            model=MODEL_NAME,
            message=prompt
        )
        # The API response includes the generated text, which we can just return.
        return response.text
    except Exception as e:
        # If something goes wrong with the API call, we'll print an error.
        return f"Failed to generate a game scenario. Error: {e}"


def get_ai_response(player_input, story_history):
    """Handles the back-and-forth conversation with the Cohere API."""
    try:
        # This is where the magic happens. We send the player's latest input
        # along with the entire conversation history.
        response = co.chat(
            model=MODEL_NAME,
            message=player_input,
            chat_history=story_history,
            # The 'preamble' is a cool feature that lets us give the AI a persona.
            # Here, we're telling it to act as a storyteller for the whole conversation.
            preamble="You are a master storyteller creating an interactive text-based adventure. Continue the story based on the user's choice. Describe the outcome and present new numbered choices."
        )
        # Just like before, we return the clean text from the response.
        return response.text
    except Exception as e:
        return f"An error occurred while getting the AI's response: {e}"

# --- Main Game Loop ---

def main():
    """This is where the game actually runs."""
    print("Welcome to the AI-driven text-based adventure game!")
    print("Type 'quit' at any time to exit.")
    
    # We need to store the conversation history to give the AI context for its responses.
    story_history = []

    # First, let's generate the opening scene.
    print("\nGenerating your adventure, please wait...")
    game_intro = generate_game_scenario()
    print("\n" + game_intro)
    
    # Add the AI's opening message to our chat history.
    # The API expects roles to be 'CHATBOT' for the AI and 'USER' for the player.
    story_history.append({"role": "CHATBOT", "message": game_intro})

    # Now, we'll start the main loop that runs until the player types 'quit'.
    while True:
        player_input = input("\n> ")
        if player_input.lower() == "quit":
            print("\nThanks for playing! Goodbye.")
            break

        # Get the AI's response based on what the player typed.
        ai_response = get_ai_response(player_input, story_history)
        print("\n" + ai_response)

        # Finally, we update our history with the player's input and the AI's response.
        # This keeps the context for the next turn.
        story_history.append({"role": "USER", "message": player_input})
        story_history.append({"role": "CHATBOT", "message": ai_response})


# This standard Python construct ensures that the main() function runs only when the script is executed directly.
if __name__ == "__main__":
    main()
