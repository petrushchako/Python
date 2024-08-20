# Requests Tutorial

### Install `requests` on local environment

    `pip install requests`


## Tutorial 

When using the `requests` library in Python to make a GET request, you can easily extract values from the response headers by accessing the `headers` attribute of the response object. The `headers` attribute is a case-insensitive dictionary that contains all the HTTP headers returned by the server.

Here’s a simple example:

```python
import requests

# Make a GET request
response = requests.get('https://example.com')

# Access the headers
headers = response.headers

# Extract a specific header value, e.g., 'Content-Type'
content_type = headers.get('Content-Type')

# Print the extracted value
print('Content-Type:', content_type)
```

### Steps:
1. **Make the GET request** using `requests.get(url)`.
2. **Access the headers** via `response.headers`. This gives you a dictionary-like object.
3. **Extract the specific header** by using the `.get('Header-Name')` method, which allows you to safely access the value without worrying about case sensitivity.

### Example of accessing multiple headers:

```python
# Extract multiple headers
content_type = headers.get('Content-Type')
server = headers.get('Server')
date = headers.get('Date')

print('Content-Type:', content_type)
print('Server:', server)
print('Date:', date)
```

### Important Notes:
- **Case Insensitivity:** HTTP headers are case-insensitive, and the `requests` library handles this automatically, so `'Content-Type'` and `'content-type'` will yield the same result.
- **.get() Method:** Using `.get()` is recommended over direct indexing (e.g., `headers['Content-Type']`) because it will return `None` if the header does not exist, rather than raising a `KeyError`.

This approach should give you easy access to any values you need from the response headers.







<br><br><hr><br>







## JSON body response
When making requests to APIs that respond with a JSON body using Python's `requests` library, you can easily parse and work with the JSON data. The `requests` library provides a built-in method called `.json()` that converts the JSON response into a Python dictionary or list, depending on the structure of the JSON.

### Example: Making a Request to an API and Parsing JSON

Let's walk through a working example where we make a request to a public API that returns a JSON response.

```python
import requests

# URL of the API endpoint
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
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
```

### Step-by-Step Breakdown:

1. **Import the `requests` library**:
   - This is necessary to use the HTTP request functionality.

2. **Define the API endpoint URL**:
   - The `url` variable holds the URL of the API endpoint.

3. **Make the GET request**:
   - Use `requests.get(url)` to send the request to the API. The `response` object will contain the server's response, including the JSON body.

4. **Check the response status**:
   - It’s good practice to check if the request was successful by examining `response.status_code`. A status code of `200` indicates success.

5. **Parse the JSON response**:
   - Use `response.json()` to convert the JSON data into a Python dictionary (`data`).

6. **Access specific data**:
   - You can access individual elements of the JSON response using the `.get()` method or standard dictionary indexing.

7. **Handle errors**:
   - If the request fails, handle the error by checking the status code and responding appropriately.

### Example Output:

When running the above example, you would see output similar to this:

```python
Post ID: 1
Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
Body: quia et suscipit
suscipit repellat nisi
tempore voluptas ...
```

### Handling Complex JSON Structures:

If the JSON response is more complex (e.g., nested dictionaries or lists), you can navigate through the data by chaining dictionary and list accesses. For example:

```python
# Example of navigating through a nested JSON response
nested_data = {
    "user": {
        "id": 1,
        "name": "John Doe",
        "details": {
            "email": "john@example.com",
            "address": {
                "city": "New York",
                "zipcode": "10001"
            }
        }
    }
}

# Accessing nested data
user_name = nested_data['user']['name']
city = nested_data['user']['details']['address']['city']

print('User Name:', user_name)
print('City:', city)
```

This approach allows you to handle any JSON structure returned by an API effectively.