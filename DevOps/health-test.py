import requests
import sys


def check_health(url):
    try:
        response = requests.get(url, timeout=3)
        print(f"Cheing health: {url}")
        print(f"Status code {response.status_code}")
        if response.status_code == 200:
            print(f"Health check successful")
        else:
            print(f"Failed or Redirect")
    except requests.exceptions.RequestException as e:
        print("Not connected or request timed out" + f"{e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide URL")
        print(f"Usage: python {sys.argv[0]} <URL>")
        sys.exit(1)
    check_health(sys.argv[1])