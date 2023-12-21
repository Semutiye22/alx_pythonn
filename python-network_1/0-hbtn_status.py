"""
This script fetches data from the intranet.hbtn.io/status URL using the requests library
and displays the response body in a tabulated format.
"""

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

# Execute the function to fetch and display the status
fetch_status()