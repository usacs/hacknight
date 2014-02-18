from flask import Flask, render_template, request, redirect
import random, string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten')
def shorten():

    #this extracts the URL parameter.
    if 'url' not in request.args:
        return 'put a damn parameter bro.'
    url = request.args['url']

    # generate a random string as the short version of this URL.

    random_str = ""
    for i in range(0, 6):
        random_str += random.choice(string.ascii_uppercase)

    with open('urls', 'a') as fh:
        fh.write(random_str + '|' + url + "\n")

    return 'your shortened url is http://localhost:5000/go?code=' + random_str

@app.route('/go')
def go():
    code = request.args['code']

    with open('urls', 'r') as fh:
        for line in fh:
            parts = line.split('|')

            if parts[0].strip() == code:
                return redirect(parts[1].strip())

    return 'your url was not found'

app.run(port=9999, debug=True)
