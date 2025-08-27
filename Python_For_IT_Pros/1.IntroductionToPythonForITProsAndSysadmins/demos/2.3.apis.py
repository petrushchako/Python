import requests

api_url = "https://api.github.com"
username = "petrushchako" # input("Enter Github username: ")
headers = {
    "Accept" : "application/vnd.github.v3+json",
    "User-Agent" : ""
}
repos_url = f"{api_url}/users/{username}/repos"


def getRepos(output):
    r = requests.get(url=repos_url, headers=headers)
    if r.status_code == 200:
        repositories = r.json()
        print(f"Repos for {username}:")

        if output:
            with open("response.json", "w")as file:
                file.write(str(repositories[0]))

        for repo in repositories:
            print(
                f"{'-'*100}\n"
                f"[{repo['name']}]\n"
                f"\tDescription: {repo['description']}\n"
                f"\tURL: {repo['owner']['repos_url']}\n"
                f"{'-'*100}"
            )


if __name__ == "__main__":
    getRepos(output=False)