import requests

def fetch_status():
    """
    Fetches data from https://intranet.hbtn.io/status using the requests library.
    Displays the response body in a tabulated format.
    """
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for key, value in data.items():
            print(f"\t- {key}: {value}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Execution starts here
fetch_status()