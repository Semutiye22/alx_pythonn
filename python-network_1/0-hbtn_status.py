import requests

url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for key, value in data.items():
        print(f"{key}:\n{' ' * 4}{value}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")