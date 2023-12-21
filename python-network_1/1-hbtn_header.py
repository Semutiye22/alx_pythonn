""" header """
import requests

if name == "__main__":
    """
    Fetches the status from the given URL using the 'requests' package and displays the body of the response.

    Uses the 'requests' package to send a GET request to the provided URL and prints the body of the response.
    """

    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)