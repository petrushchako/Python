import requests

# URL of the API endpoint
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(response.text)
    # Parse the JSON response into a Python dictionary
    data = response.json()

    # Access specific data from the JSON
    post_id = data.get('id')
    title = data.get('title')
    body = data.get('body')

    # Print the extracted data
    print('Post ID:', post_id)
    print('Title:', title)
    print('Body:', body)
else:
    print('Failed to retrieve data:', response.status_code)