import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the token from an environment variable
token = os.getenv("GITHUB_TOKEN")

# print(token)

# GitHub API endpoint for user information
url = "https://api.github.com/user"

# Set up the headers with the authorization token
headers = {"Authorization": f"token {token}"}

# Make the GET request to the GitHub API
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    user_data = response.json()

    # Access specific data from the JSON
    username = user_data.get("login")
    name = user_data.get("name")
    public_repos = user_data.get("public_repos")

    # Print the extracted data
    print("Username:", username)
    print("Name:", name)
    print("Public Repositories:", public_repos)

else:
    print("Failed to retrieve data:", response.status_code)


# Print list of repos

username = "petrushchako"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    repos = response.json()

    print(f"{username} repositories:")

    with open("response.json", "w") as file:
        json.dump(repos, file, indent=4)

    for repo in repos:
        print(f"\t {repo['name']}")

else:
    print("Failed to retrieve data:", response.status_code)
