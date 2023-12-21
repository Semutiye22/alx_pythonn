import requests
import sys

if len(sys.argv) < 3:
    print("Please provide a URL and an email address.")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

payload = {'email': email}
response = requests.post(url, data=payload)

if response.status_code == 200:
    print("Response Body:")
    print(response.text)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")