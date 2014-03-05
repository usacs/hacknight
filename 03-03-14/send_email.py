import requests, sys

payload = { "api_user" : "YOU SENDGRID USERNAME", \
            "api_key"  : "YOUR SENDGRID PASSWORD", \
            "to"       : sys.argv[1], \
            "from"     : sys.argv[2], \
            "subject"  : "Playing with an API", \
            "text"     : sys.argv[3] }

response = requests.post("https://api.sendgrid.com/api/mail.send.json", data = payload)

print response

"""
This code makes a POST request to SendGrid's API to send an email!
Be sure to fill in your username and password.
It is ran like this:
python send_email.py to@youremail.com from@youremail.com "The text of the email!"
"""
