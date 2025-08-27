import requests

api_url = "https://api.github.com"
username = "petrushchako" # input("Enter Github username: ")

headers = {
    "Accept" : "application/vnd.github.v3+json",
    "User-Agent" : ""
}

repos_url = f"{api_url}/users/{username}/repos"
r = requests.get(url=repos_url, headers=headers)

if r.status_code == 200:
    repositories = r.json()
    print(f"Repos for {username}:")
    with open("response.json", "w")as file:
        file.write(str(repositories[0]))
    #print(len(repositories))
    for repo in repositories:
        print(f"{"-"*100}\n[{repo["name"]}]\n\tDescription: {repo["description"]}\n\tURL: {repo["owner"]["repos_url"]}\n{"-"*100}")