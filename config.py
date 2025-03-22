import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

dotenv_path = os.path.join('.venv', '.env')

# Load the .env file explicitly
load_dotenv(dotenv_path)

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)
