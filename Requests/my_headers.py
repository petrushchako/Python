import requests

r = requests.get("https://xkcd.com/353/")

print(r)  # <Response [200]>
# print(dir(r))
# print(r.headers)
headers = r.headers

# Extract values from headers obj
print(headers.get("Expires"))

print(r.text)
