from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        res = "Hello, " + request.form['name'] + ". You made a POST request\n"
        return Response(status=200, response=res)
    return "You made a GET request!\n"

if __name__ == "__main__":
    app.debug = True
    app.run()

"""
Test the app using curl!

To make a GET request using curl:
curl -X GET localhost:5000

To make a POST request with your name as data:
curl -X POST localhost:5000 -d "name=your name"
"""
