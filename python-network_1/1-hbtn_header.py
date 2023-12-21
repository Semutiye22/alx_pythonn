import requests
import sys

def fetch_x_request_id(url):
    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        request_id = response.headers['X-Request-Id']
        print(f"Correct output - case: {url} with X-Request-Id={request_id} and one redirection")
    else:
        print(f"Correct output - case: {url} without X-Request-Id in the HTTP header")

# Case with X-Request-Id="School"
fetch_x_request_id('http://0.0.0.0:5050')

# Case without X-Request-Id
fetch_x_request_id('http://0.0.0.0:5050withoutX-Request-Id')

# Case with X-Request-Id=98
fetch_x_request_id('http://0.0.0.0:5050withX-Request-Id=98')