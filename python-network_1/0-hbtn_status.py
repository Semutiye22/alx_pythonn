import requests

# Define the URL to fetch data from
url = 'https://alu-intranet.hbtn.io/status'

# Send a GET request to the URL
response = requests.get(url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()
    
    # Display the fetched data in a specific format
    print("- id: {}".format(data.get('id')))
    print("  - name: {}".format(data.get('name')))
    print("  - description: {}".format(data.get('description')))
    print("  - status: {}".format(data.get('status')))
else:
    # Print an error message if fetching fails
    print("Failed to fetch data. Status code: {}".format(response.status_code))