# CSD 325: Advanced Python
# Module 9.2 Assignment: APIs
# Isaac Ellingson
# 11/30/2025

from datetime import datetime
import random
import requests
import json

# These are backup facts saved from a secondary source at https://www.chucknorrisfacts.net/
# They will only be provided if we can't reach the primary source for some reason.
BACKUP_FACTS = (
    "Chuck Norris caught the Coronavirus. He keeps it chained in his back yard.",
    "Chuck Norris won the Tour de France with a stationary bicycle.",
    "Chuck Norris doesn't have any enemies. Well, not any more.",
    "Chuck Norris grocery shops at the Home Depot",
    "A toll booth pays Chuck Norris to pass"
    )

def print_local_fact():
    print("Online facts are unavailable. Please enjoy this local Chuck Norris Fact:")
    print(random.choice(BACKUP_FACTS))



try:
    # This is typically an https api, but the requests module can't handle secure connections

    # Unfortunately this endpoint can sometimes produce some off-color responses,
    # since it is sourced from user submissions.
    response = requests.get("http://api.chucknorris.io/jokes/random")

    # Anything other than a 200 status, INCLUDING a redirect, is going to be a problem
    # for our simple code here, so just raise it as an exception.
    if (response.status_code != 200):
        response.raise_for_status()

    fact = response.json()['value']
    # ISO dates weren't very user friendly so I did some massaging here
    date = datetime.fromisoformat(response.json()['created_at']).strftime("%A, %d %B %Y %I:%M%p")

    print("Please enjoy this Chuck Norris Fact:")
    print(fact + " (created on " + date + ")")

# For pretty much all errors we want to supply a backup fact from our short list above.
except requests.exceptions.Timeout:
    print("The request timed out. The server took too long to respond.")
    print_local_fact()
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
    print_local_fact()
except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")
    print_local_fact()
