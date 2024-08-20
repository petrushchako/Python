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