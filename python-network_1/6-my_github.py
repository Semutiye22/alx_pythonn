import requests
import sys

if len(sys.argv) < 3:
    print("Please provide your username and personal access token.")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
url = 'https://api.github.com/user'

response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    user_info = response.json()
    user_id = user_info.get('id')
    if user_id:
        print(f"Your GitHub user ID is: {user_id}")
    else:
        print("User ID not found in the response.")
else:
    print(f"Failed to fetch user data. Status code: {response.status_code}")
     
    
