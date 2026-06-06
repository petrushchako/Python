import requests
import sys


def check_health(url):
    # Ensure the URL has a scheme; if not, default to http://
    if not url.startswith(("http://", "https://")):
        request_url = "http://" + url
    else:
        request_url = url

    try:
        print(f"Checking health: {request_url}")
        response = requests.get(request_url, timeout=3)
        print(f"Status code: {response.status_code}")

        if response.status_code == 200:
            print("Health check successful")
        else:
            print("Failed or Redirect")

    except requests.exceptions.RequestException as e:
        print("Not connected or request timed out" + f"{e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide URL")
        print(f"Usage: python {sys.argv[0]} <URL>")
        sys.exit(1)
    check_health(sys.argv[1])