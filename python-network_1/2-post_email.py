import requests
import sys

if name == "__main__":
    """
    Sends a request to a given URL and displays the value of the variable X-Request-Id in the response header.

    Takes a URL as input, sends a request to the URL using the 'requests' package, 
    and displays the value of the X-Request-Id variable found in the response header.
    """

    url = sys.argv[1]  # Fetching URL from command line argument

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)