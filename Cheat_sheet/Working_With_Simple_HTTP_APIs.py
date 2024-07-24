""" Working With Simple HTTP APIs  """

# 1. Basic GET Request
# To fetch data from an API endpoint using a GET request:

import requests
response = requests.get('https://api.example.com/data')
data = response.json()  # Assuming the response is JSON
print(data)

# 2. GET Request with Query Parameters
# To send a GET request with query parameters:

import requests
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://api.example.com/search', params=params)
data = response.json()
print(data)

# 3. Handling HTTP Errors
# To handle possible HTTP errors gracefully:

import requests
response = requests.get('https://api.example.com/data')
try:
    response.raise_for_status()  # Raises an HTTPError if the status is 4xx, 5xx
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as err:
    print(f'HTTP Error: {err}')


# 4. Setting Timeout for Requests
# To set a timeout for API requests to avoid hanging indefinitely:

import requests
try:
    response = requests.get('https://api.example.com/data', timeout=5)  # Timeout in seconds
    data = response.json()
    print(data)
except requests.exceptions.Timeout:
    print('The request timed out')

# 5. Using Headers in Requests
# To include headers in your request (e.g., for authorization):

import requests
headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
response = requests.get('https://api.example.com/protected', headers=headers)
data = response.json()
print(data)

# 6. POST Request with JSON Payload
T# o send data to an API endpoint using a POST request with a JSON payload:

import requests
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'Content-Type': 'application/json'}
response = requests.post('https://api.example.com/submit', json=payload, headers=headers)
print(response.json())

# 7. Handling Response Encoding
# To handle the response encoding properly:

import requests
response = requests.get('https://api.example.com/data')
response.encoding = 'utf-8'  # Set encoding to match the expected response format
data = response.text
print(data)

# 8. Using Sessions with Requests
# To use a session object for making multiple requests to the same host, which can improve performance:

import requests
with requests.Session() as session:
    session.headers.update({'Authorization': 'Bearer YOUR_ACCESS_TOKEN'})
    response = session.get('https://api.example.com/data')
    print(response.json())

# 9. Handling Redirects
# To handle or disable redirects in requests:

import requests
response = requests.get('https://api.example.com/data', allow_redirects=False)
print(response.status_code)

# 10. Streaming Large Responses
# To stream a large response to process it in chunks, rather than loading it all into memory:

import requests
response = requests.get('https://api.example.com/large-data', stream=True)
for chunk in response.iter_content(chunk_size=1024):
    process(chunk)  # Replace 'process' with your actual processing function




