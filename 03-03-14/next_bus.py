import requests, json

response = requests.get("http://runextbus.herokuapp.com/active")

for item in response.json()['routes']:
    print item['title']

"""
This example makes a GET request to the Rutgers Next Bus API of active busses.
It then iterates through the JSON response and prints out the name of the bus
route using the appropriate keys.

It is run simply as:
python next_busy.py
"""
