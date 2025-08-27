import requests
from bs4 import BeautifulSoup # type: ignore

"""
BeautifulSoup4 documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
"""

url = "https://www.crummy.com/software/BeautifulSoup/"

r = requests.get(url)

if r.status_code == 200:
    soup = BeautifulSoup(r.content, "html.parser")
    headers = soup.find_all("a")

    for header in headers:
        print(header.get("href"))
else:
    print(f"Response status: {r.status_code}")
