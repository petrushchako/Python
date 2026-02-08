import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access variables
api_key = os.getenv("API_KEY")
debug = os.getenv("DEBUG")
port = os.getenv("PORT")

# Print variables
print(f"{api_key=}")
print(f"{debug=}")
print(f"{port=}")
