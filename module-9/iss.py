# CSD 325: Advanced Python
# Module 9.2 Assignment: APIs
# Isaac Ellingson
# 11/30/2025

import requests
import json

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

try:
    response = requests.get("http://api.open-notify.org/astros.json", timeout=5)
    response.raise_for_status()  # Raises an exception for 4xx or 5xx status codes
    jprint(response.json())
except requests.exceptions.Timeout:
    print("The request timed out. The server took too long to respond.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")
