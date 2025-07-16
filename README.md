AI Text-Based Adventure Game
This is an AI-driven text-based adventure game where the player interacts with an AI to progress through a dynamically generated story. The game uses the Cohere API to create unique scenarios and responses, ensuring no two playthroughs are the same.

Installation & Setup
1️⃣ Clone the repository:

git clone https://github.com/NithishKumarPuppala/AI-driven-Text-game.git
cd AI-driven-Text-game

2️⃣ Install dependencies:
Create a requirements.txt file with the following content:

cohere
python-dotenv

Then, install the required packages using pip:

pip install -r requirements.txt

3️⃣ Set up the API key:

Create a file named .env in the project's root directory.

Add your Cohere API key to the .env file like this:

COHERE_API_KEY="your-cohere-api-key-here"

(Replace your-cohere-api-key-here with your actual Cohere API key).

4️⃣ Run the game:

python game.py

Type 'quit' anytime to exit the game.

Notes
Requires Python 3.x.

Uses the Cohere API for generating all game content.

The .env file is included in .gitignore to keep your API key secure and private.