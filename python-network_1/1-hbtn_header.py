import requests
import sys

if len(sys.argv) < 2:
    print("Please provide a URL.")
    sys.exit(1)

url = sys.argv[1]
response = requests.get(url)

if response.status_code == 200:
    request_id = response.headers.get('X-Request-Id')
    if request_id:
        print(f"X-Request-Id value: {request_id}")
    else:
        print("X-Request-Id header not found in the response.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")